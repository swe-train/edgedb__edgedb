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


class AccessPolicyMixin:

    def get_condition(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'condition')
        return cast(expr.Expression, val)

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_action(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.AccessPolicyAction':
        val = s_orm.get_field_value(self, schema, 'action')
        return cast(qltypes.AccessPolicyAction, val)

    def get_access_kinds(
        self, schema: 's_schema.Schema'
    ) -> 'objects.MultiPropSet[qltypes.AccessKind]':
        val = s_orm.get_field_value(self, schema, 'access_kinds')
        return cast(objects.MultiPropSet[qltypes.AccessKind], val)

    def get_subject(
        self, schema: 's_schema.Schema'
    ) -> 'objects.InheritingObject':
        val = s_orm.get_field_value(self, schema, 'subject')
        return cast(objects.InheritingObject, val)

    def get_errmessage(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'errmessage')
        return cast(str, val)

    def get_owned(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'owned')
        return cast(bool, val)
