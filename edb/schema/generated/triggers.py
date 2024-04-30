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
from edb.edgeql import qltypes


class TriggerMixin:

    def get_timing(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.TriggerTiming':
        val = s_orm.get_field_value(self, schema, 'timing')
        return cast(qltypes.TriggerTiming, val)

    def get_kinds(
        self, schema: 's_schema.Schema'
    ) -> 'objects.MultiPropSet[qltypes.TriggerKind]':
        val = s_orm.get_field_value(self, schema, 'kinds')
        return cast(objects.MultiPropSet[qltypes.TriggerKind], val)

    def get_scope(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.TriggerScope':
        val = s_orm.get_field_value(self, schema, 'scope')
        return cast(qltypes.TriggerScope, val)

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_condition(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'condition')
        return cast(expr.Expression, val)

    def get_subject(
        self, schema: 's_schema.Schema'
    ) -> 'objects.InheritingObject':
        val = s_orm.get_field_value(self, schema, 'subject')
        return cast(objects.InheritingObject, val)

    def get_owned(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'owned')
        return cast(bool, val)
