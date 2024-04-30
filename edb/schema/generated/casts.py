# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.edgeql import ast
from edb.schema import types


class CastMixin:

    def get_from_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'from_type')
        return cast(types.Type, val)

    def get_to_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'to_type')
        return cast(types.Type, val)

    def get_allow_implicit(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'allow_implicit')
        return cast(bool, val)

    def get_allow_assignment(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'allow_assignment')
        return cast(bool, val)

    def get_language(
        self, schema: 's_schema.Schema'
    ) -> 'ast.Language':
        val = s_orm.get_field_value(self, schema, 'language')
        return cast(ast.Language, val)

    def get_from_function(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'from_function')
        return cast(str, val)

    def get_from_expr(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'from_expr')
        return cast(bool, val)

    def get_from_cast(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'from_cast')
        return cast(bool, val)

    def get_code(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'code')
        return cast(str, val)
