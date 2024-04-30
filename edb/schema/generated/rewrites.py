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


class RewriteMixin:

    def get_kind(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.RewriteKind':
        val = s_orm.get_field_value(self, schema, 'kind')
        return cast(qltypes.RewriteKind, val)

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_subject(
        self, schema: 's_schema.Schema'
    ) -> 'objects.InheritingObject':
        val = s_orm.get_field_value(self, schema, 'subject')
        return cast(objects.InheritingObject, val)
