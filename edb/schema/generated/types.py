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
from edb.schema import types


class TypeMixin:

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_expr_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.ExprType':
        val = s_orm.get_field_value(self, schema, 'expr_type')
        return cast(types.ExprType, val)

    def get_from_alias(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'from_alias')
        return cast(bool, val)

    def get_from_global(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'from_global')
        return cast(bool, val)

    def get_alias_is_persistent(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'alias_is_persistent')
        return cast(bool, val)

    def get_rptr(
        self, schema: 's_schema.Schema'
    ) -> 'objects.Object':
        val = s_orm.get_field_value(self, schema, 'rptr')
        return cast(objects.Object, val)

    def get_backend_id(
        self, schema: 's_schema.Schema'
    ) -> 'int':
        val = s_orm.get_field_value(self, schema, 'backend_id')
        return cast(int, val)

    def get_transient(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'transient')
        return cast(bool, val)


class QualifiedTypeMixin:
    pass

class InheritingTypeMixin:
    pass

class CollectionMixin:

    def get_is_persistent(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'is_persistent')
        return cast(bool, val)


class CollectionExprAliasMixin:
    pass

class ArrayMixin:

    def get_element_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'element_type')
        return cast(types.Type, val)

    def get_dimensions(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedList[int]':
        val = s_orm.get_field_value(self, schema, 'dimensions')
        return cast(checked.FrozenCheckedList[int], val)


class ArrayExprAliasMixin:
    pass

class TupleMixin:

    def get_named(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'named')
        return cast(bool, val)

    def get_element_types(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectDict[str, types.Type]':
        val = s_orm.get_field_value(self, schema, 'element_types')
        return cast(objects.ObjectDict[str, types.Type], val)


class TupleExprAliasMixin:
    pass

class RangeMixin:

    def get_element_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'element_type')
        return cast(types.Type, val)


class RangeExprAliasMixin:
    pass

class MultiRangeMixin:

    def get_element_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'element_type')
        return cast(types.Type, val)


class MultiRangeExprAliasMixin:
    pass