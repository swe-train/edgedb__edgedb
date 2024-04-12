# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.edgeql import ast
from edb.schema import abc
from edb.schema import functions
from edb.schema import types

class Cast(
    objects.QualifiedObject,
    annos.AnnotationSubject,
    functions.VolatilitySubject,
    abc.Cast
):

    def get_from_type(
        self, schema: s_schema.Schema
    ) -> types.Type: ...

    def get_to_type(
        self, schema: s_schema.Schema
    ) -> types.Type: ...

    def get_allow_implicit(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_allow_assignment(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_language(
        self, schema: s_schema.Schema
    ) -> ast.Language: ...

    def get_from_function(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_from_expr(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_from_cast(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_code(
        self, schema: s_schema.Schema
    ) -> str: ...
