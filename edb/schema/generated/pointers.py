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
from edb.schema import pointers
from edb.schema import rewrites
from edb.schema import expr
from edb.schema import types


class PointerMixin:

    def get_source(
        self, schema: 's_schema.Schema'
    ) -> 'objects.InheritingObject':
        val = s_orm.get_field_value(self, schema, 'source')
        return cast(objects.InheritingObject, val)

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

    def get_readonly(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'readonly')
        return cast(bool, val)

    def get_secret(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'secret')
        return cast(bool, val)

    def get_protected(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'protected')
        return cast(bool, val)

    def get_computable(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'computable')
        return cast(bool, val)

    def get_from_alias(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'from_alias')
        return cast(bool, val)

    def get_defined_here(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'defined_here')
        return cast(bool, val)

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

    def get_cardinality(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.SchemaCardinality':
        val = s_orm.get_field_value(self, schema, 'cardinality')
        return cast(qltypes.SchemaCardinality, val)

    def get_union_of(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[pointers.Pointer]':
        val = s_orm.get_field_value(self, schema, 'union_of')
        return cast(objects.ObjectSet[pointers.Pointer], val)

    def get_intersection_of(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[pointers.Pointer]':
        val = s_orm.get_field_value(self, schema, 'intersection_of')
        return cast(objects.ObjectSet[pointers.Pointer], val)

    def get_computed_link_alias_is_backward(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'computed_link_alias_is_backward')
        return cast(bool, val)

    def get_computed_link_alias(
        self, schema: 's_schema.Schema'
    ) -> 'objects.Object':
        val = s_orm.get_field_value(self, schema, 'computed_link_alias')
        return cast(objects.Object, val)

    def get_rewrites(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectIndexByUnqualifiedName[rewrites.Rewrite]':
        val = s_orm.get_field_value(self, schema, 'rewrites')
        return cast(objects.ObjectIndexByUnqualifiedName[rewrites.Rewrite], val)
