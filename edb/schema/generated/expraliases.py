# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.schema import expr
from edb.schema import types


class AliasMixin:

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'type')
        return cast(types.Type, val)

    def get_created_types(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[types.Type]':
        val = s_orm.get_field_value(self, schema, 'created_types')
        return cast(objects.ObjectSet[types.Type], val)
