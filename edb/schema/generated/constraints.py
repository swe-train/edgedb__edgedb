# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.common import checked
from edb.schema import expr
from edb.schema import constraints
from edb.schema import functions


class ConstraintMixin:

    def get_params(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[functions.Parameter]':
        val = s_orm.get_field_value(self, schema, 'params')
        return cast(objects.ObjectList[functions.Parameter], val)

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_subjectexpr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'subjectexpr')
        return cast(expr.Expression, val)

    def get_finalexpr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'finalexpr')
        return cast(expr.Expression, val)

    def get_except_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'except_expr')
        return cast(expr.Expression, val)

    def get_subject(
        self, schema: 's_schema.Schema'
    ) -> 'objects.Object':
        val = s_orm.get_field_value(self, schema, 'subject')
        return cast(objects.Object, val)

    def get_args(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedList[expr.Expression]':
        val = s_orm.get_field_value(self, schema, 'args')
        return cast(checked.FrozenCheckedList[expr.Expression], val)

    def get_delegated(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'delegated')
        return cast(bool, val)

    def get_errmessage(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'errmessage')
        return cast(str, val)

    def get_is_aggregate(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'is_aggregate')
        return cast(bool, val)


class ConsistencySubjectMixin:

    def get_constraints(
        self, schema: 's_schema.Schema'
    ) -> 'constraints.ObjectIndexByConstraintName[constraints.Constraint]':
        val = s_orm.get_field_value(self, schema, 'constraints')
        return cast(constraints.ObjectIndexByConstraintName[constraints.Constraint], val)
