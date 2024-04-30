# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import expr
from edb.common import checked


class ScalarTypeMixin:

    def get_default(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'default')
        return cast(expr.Expression, val)

    def get_enum_values(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedList[str]':
        val = s_orm.get_field_value(self, schema, 'enum_values')
        return cast(checked.FrozenCheckedList[str], val)

    def get_sql_type(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'sql_type')
        return cast(str, val)

    def get_sql_type_scheme(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'sql_type_scheme')
        return cast(str, val)

    def get_num_params(
        self, schema: 's_schema.Schema'
    ) -> 'int':
        val = s_orm.get_field_value(self, schema, 'num_params')
        return cast(int, val)

    def get_arg_values(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedList[str]':
        val = s_orm.get_field_value(self, schema, 'arg_values')
        return cast(checked.FrozenCheckedList[str], val)
