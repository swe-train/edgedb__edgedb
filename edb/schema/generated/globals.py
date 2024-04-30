# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.edgeql import qltypes
from edb.schema import expr
from edb.schema import types


class GlobalMixin:

    def get_target(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'target')
        return cast(types.Type, val)

    def get_required(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'required')
        return cast(bool, val)

    def get_cardinality(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.SchemaCardinality':
        val = s_orm.get_field_value(self, schema, 'cardinality')
        return cast(qltypes.SchemaCardinality, val)

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_default(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'default')
        return cast(expr.Expression, val)

    def get_created_types(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[types.Type]':
        val = s_orm.get_field_value(self, schema, 'created_types')
        return cast(objects.ObjectSet[types.Type], val)
