# Copyright 2023 jothepro
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from pathlib import Path

import arpeggio
from arpeggio import PTNodeVisitor
from arpeggio import visit_parse_tree
from arpeggio.cleanpeg import ParserPEG

from pydjinni.defs import IDL_GRAMMAR_PATH
from pydjinni.exceptions import FileNotFoundException, ApplicationException
from pydjinni.file.file_reader_writer import FileReaderWriter
from pydjinni.generator.cpp.cpp.generator import CppGenerator
from pydjinni.generator.target import Target
from pydjinni.position import Position, Cursor
from .ast import *
from .base_models import BaseExternalType
from .identifier import IdentifierType as Identifier
from .resolver import Resolver


def unpack(list_input: []):
    return list_input[0] if list_input else None


class IdlParser(PTNodeVisitor):
    def __init__(
            self,
            resolver: Resolver,
            targets: list[Target],
            supported_target_keys: list[str],
            include_dirs: list[Path],
            default_deriving: set[Record.Deriving],
            file_reader: FileReaderWriter,
            idl: Path,
            position: Position = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.idl_parser = ParserPEG(IDL_GRAMMAR_PATH.read_text(), root_rule_name="idl")
        self.resolver = resolver
        self.targets = targets
        self.target_keys = supported_target_keys
        self.file_reader = file_reader
        self.include_dirs = include_dirs
        self.default_deriving = default_deriving
        self.idl = idl
        self.position = position
        self.type_defs: list[BaseType] = []
        self.field_defs: list[BaseField] = []
        self.current_namespace: list[Identifier] = []
        self.current_namespace_stack_size: list[int] = []

    class ParsingException(ApplicationException, code=150):
        """IDL Parsing error"""

    def visit_type_def(self, node, children) -> BaseType:
        type_def = unpack(children)
        self.resolver.register(type_def)
        self.type_defs.append(type_def)
        return type_def

    def visit_enum(self, node, children):
        enum = Enum(
            name=unpack(children.identifier),
            position=self._position(node),
            items=children.item,
            namespace=self.current_namespace
        )
        if children.comment:
            enum.comment = unpack(children.comment)
        return enum

    def visit_flags(self, node, children):
        flags = Flags(
            name=unpack(children.identifier),
            position=self._position(node),
            flags=children.flag,
            namespace=self.current_namespace
        )
        if children.comment:
            flags.comment = unpack(children.comment)
        return flags

    def visit_flag(self, node, children):
        all = unpack(children.flag_modifier) == 'all' if children.flag_modifier else False
        none = unpack(children.flag_modifier) == 'none' if children.flag_modifier else False
        flag = Flags.Flag(
            name=unpack(children.identifier),
            position=self._position(node),
            comment=unpack(children.comment),
            all=all,
            none=none
        )
        self.field_defs.append(flag)
        return flag

    def visit_flag_modifier(self, node, children):
        return children[0]

    def visit_interface(self, node, children):
        methods: list[Interface.Method] = children.method
        properties: list[Interface.Property] = children.property
        dependencies: list[TypeReference] = []

        for method in methods:
            for param in method.parameters:
                dependencies.append(param.type_ref)
            if method.return_type_ref:
                dependencies.append(method.return_type_ref)
        for property_def in properties:
            dependencies.append(property_def.type_ref)
        return Interface(
            name=unpack(children.identifier),
            position=self._position(node),
            methods=methods,
            targets=unpack(children.targets) or self.target_keys,
            properties=properties,
            main='main' in children.results,
            namespace=self.current_namespace,
            dependencies=self._dependencies(dependencies),
            comment=unpack(children.comment)
        )

    def second_interface(self, interface: Interface):
        if interface.main and interface.targets != [CppGenerator.key]:
            raise IdlParser.ParsingException("a 'main' interface can only be implemented in C++", interface.position)

        for method in interface.methods:
            if CppGenerator.key not in interface.targets and method.static:
                raise IdlParser.ParsingException(
                    f"methods are only allowed to be static on '{CppGenerator.key}' interfaces",
                    interface.position
                )

    def visit_named_function(self, node, children):
        function = unpack(children.function)
        function.name = unpack(children.identifier)
        function.comment = unpack(children.comment)
        function.position = self._position(node)
        function.anonymous = False
        return function

    def visit_function(self, node, children):
        targets: list[str] = unpack(children.targets) or self.target_keys
        return_type_ref = unpack(children.type_ref)
        parameters = children.parameter

        dependencies: list[TypeReference] = []

        for param in parameters:
            dependencies.append(param.type_ref)
        if return_type_ref:
            dependencies.append(return_type_ref)

        def signature(type_ref: TypeReference, depth: int = 2):
            output = type_ref.name
            generic_signatures = []
            for param in type_ref.parameters:
                generic_signatures.append(signature(param, depth + 1))
            return ('_' * depth).join([output] + generic_signatures)

        name = '_'.join(
            ['function'] +
            [signature(parameter.type_ref) for parameter in parameters] +
            [signature(return_type_ref) if return_type_ref else 'void']
        )
        return Function(
            name=name,
            position=self._position(node),
            parameters=parameters,
            targets=targets,
            namespace=self.current_namespace,
            return_type_ref=return_type_ref,
            dependencies=dependencies
        )

    def visit_identifier(self, node, children):
        return Identifier(node.value)

    def visit_deriving(self, node, children):
        return set(children.declaration)

    def visit_declaration(self, node, children):
        try:
            return Record.Deriving(node.value)
        except ValueError:
            raise IdlParser.ParsingException(
                f"{node.value} is not a valid record deriving", self._position(node))

    def visit_record(self, node, children):
        targets = unpack(children.targets) or []
        fields: list[Record.Field] = children.field
        deriving = unpack(children.deriving) or set()
        record = Record(
            name=unpack(children.identifier),
            position=self._position(node),
            fields=fields,
            targets=targets,
            namespace=self.current_namespace,
            dependencies=self._dependencies([field.type_ref for field in fields]),
            deriving=deriving | self.default_deriving
        )
        if children.comment:
            record.comment = unpack(children.comment)
        return record

    def visit_data_type(self, node, children):
        parameters = children.data_type or []
        return TypeReference(
            name=str(node[0]),
            parameters=parameters,
            position=self._position(node),
            namespace=self.current_namespace,
            optional='optional' in children.results
        )

    def visit_type_ref(self, node, children) -> TypeReference:
        output = unpack(children)
        if isinstance(output, Function):
            type_def = unpack(children.function)
            self.type_defs.append(type_def)
            output = TypeReference(
                name="<function>",
                position=self._position(node),
                type_def=type_def,
                namespace=self.current_namespace
            )
        return output

    def second_data_type(self, type_ref: TypeReference):
        if not type_ref.type_def:
            type_ref.type_def = self.resolver.resolve(type_ref)
            if type_ref.parameters and not type_ref.type_def.params:
                raise IdlParser.ParsingException(
                    f"Type '{type_ref.name}' does not accept generic parameters",
                    type_ref.position
                )
            elif type_ref.parameters and len(type_ref.type_def.params) != len(type_ref.parameters):
                expected_parameters = ", ".join(type_ref.type_def.params)
                raise IdlParser.ParsingException(
                    f"Invalid number of generic parameters given to '{type_ref.name}'. "
                    f"Expects {len(type_ref.type_def.params)} ({expected_parameters}), "
                    f"but {len(type_ref.parameters)} where given.",
                    type_ref.position
                )

    def visit_item(self, node, children):
        item = Enum.Item(
            name=unpack(children.identifier),
            position=self._position(node),
            comment=unpack(children.comment)
        )
        self.field_defs.append(item)
        return item

    def visit_method(self, node, children):
        return Interface.Method(
            name=unpack(children.identifier),
            position=self._position(node),
            comment=unpack(children.comment),
            parameters=children.parameter,
            return_type_ref=unpack(children.type_ref),
            static='static' in children,
            const='const' in children,
        )

    def second_method(self, method: Interface.Method):
        self.field_defs.append(method)
        if method.static and method.const:
            raise IdlParser.ParsingException("method cannot be both static and const", method.position)

    def visit_property(self, node, children):
        return Interface.Property(
            name=unpack(children.identifier),
            type_ref=unpack(children.type_ref),
            comment=unpack(children.comment),
            position=self._position(node)
        )

    def second_property(self, decl: Interface.Property):
        self.field_defs.append(decl)

    def visit_parameter(self, node, children):
        return Parameter(
            name=unpack(children.identifier),
            position=self._position(node),
            type_ref=unpack(children.type_ref)
        )

    def second_parameter(self, param: Parameter):
        self.field_defs.append(param)

    def visit_targets(self, node, children):
        includes = []
        excludes = []
        if "+any" in children:
            includes = self.target_keys
        for item in children:
            if item.startswith('+'):
                includes.append(item[1:])
            else:
                excludes.append(item[1:])
        if (not includes) and excludes:
            includes = self.target_keys

        targets = [include for include in includes if include not in excludes]
        for target in targets:
            if target not in self.target_keys:
                raise IdlParser.ParsingException(
                    f"Unknown interface target '{target}'",
                    self._position(node)
                )
        return targets

    def visit_field(self, node, children):
        return Record.Field(
            name=unpack(children.identifier),
            position=self._position(node),
            comment=unpack(children.comment),
            type_ref=unpack(children.type_ref)
        )

    def second_field(self, field: Record.Field):
        self.field_defs.append(field)
        if field.type_ref.type_def.primitive == BaseExternalType.Primitive.function:
            raise IdlParser.ParsingException("functions are not allowed as record field type.", field.position)

    def visit_comment(self, node, children):
        return "\n".join([child[1:] for child in children])

    def visit_filepath(self, node, children):
        path = Path(node.value[1:-1])
        search_paths = [path] + [include_dir / path for include_dir in self.include_dirs]
        for search_path in search_paths:
            if search_path.exists():
                return search_path
        raise FileNotFoundException(path)

    def _dependencies(self, type_refs: list[TypeReference]) -> list[TypeReference]:
        output: list[TypeReference] = []
        for type_ref in type_refs:
            output.append(type_ref)
            output += self._dependencies(type_ref.parameters)
        return output

    def visit_import_def(self, node, children):
        ast = IdlParser(
            resolver=self.resolver,
            targets=self.targets,
            supported_target_keys=self.target_keys,
            include_dirs=self.include_dirs,
            default_deriving=self.default_deriving,
            file_reader=self.file_reader,
            idl=unpack(children.filepath),
            position=self._position(node)).parse()
        self.type_defs += ast
        return ast

    def visit_extern(self, node, children):
        self.resolver.load_external(unpack(children.filepath))

    def visit_begin_namespace(self, node, children):
        self.current_namespace += children.identifier
        self.current_namespace_stack_size.append(len(children.identifier))

    def visit_end_namespace(self, node, children):
        for _ in range(self.current_namespace_stack_size.pop()):
            self.current_namespace.pop()

    def _position(self, node) -> Position:
        line_start, col_start = self.idl_parser.pos_to_linecol(node.position)
        line_end, col_end = self.idl_parser.pos_to_linecol(node.position_end)
        return Position(
            start=Cursor(line=line_start, col=col_start),
            end=Cursor(line=line_end, col=col_end),
            file=self.idl
        )

    def parse(self) -> list[BaseType]:
        """
        Parses the given input with `arpeggio`.

        - Creates the AST from the given IDL file.
        - Tries to resolve all type references.

        Args:
            idl: Path to the IDL file that should be parsed
            position: The position of the @import statement, if the method is called recursively by an import

        Returns:
            The parsed Abstract Syntax Tree (AST)

        Raises:
            IdlParser.ParsingException       : When the input could not be parsed.
            IdlParser.TypeResolvingException : When a referenced type cannot be found.
            IdlParser.DuplicateTypeException : When a type is re-declared.
        """
        try:
            parse_tree = self.idl_parser.parse(self.file_reader.read_idl(self.idl))
            ast = visit_parse_tree(parse_tree, self)
            for target in self.targets:
                target.marshal(self.type_defs, self.field_defs)
            return self.type_defs
        except FileNotFoundError as e:
            raise FileNotFoundException(Path(e.filename))
        except arpeggio.NoMatch as e:
            e.eval_attrs()
            raise IdlParser.ParsingException(e.message, Position(file=self.idl, start=Cursor(line=e.line, col=e.col)))
        except RecursionError:
            raise IdlParser.ParsingException(
                f"Recursive Import detected: file {self.idl} imports itself!",
                self.position
            )
