# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
import uuid
from edb.common import span
from edb.schema import name
from edb.schema import objects
from edb.common import checked


class ObjectMixin:

    def get_id(
        self, schema: 's_schema.Schema'
    ) -> 'uuid.UUID':
        val = s_orm.get_field_value(self, schema, 'id')
        return cast(uuid.UUID, val)

    def get_internal(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'internal')
        return cast(bool, val)

    def get_sourcectx(
        self, schema: 's_schema.Schema'
    ) -> 'span.Span':
        val = s_orm.get_field_value(self, schema, 'sourcectx')
        return cast(span.Span, val)

    def get_name(
        self, schema: 's_schema.Schema'
    ) -> 'name.Name':
        val = s_orm.get_field_value(self, schema, 'name')
        return cast(name.Name, val)

    def get_builtin(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'builtin')
        return cast(bool, val)

    def get_computed_fields(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedSet[str]':
        val = s_orm.get_field_value(self, schema, 'computed_fields')
        return cast(checked.FrozenCheckedSet[str], val)


class InternalObjectMixin:
    pass

class QualifiedObjectMixin:

    def get_name(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        val = s_orm.get_field_value(self, schema, 'name')
        return cast(name.QualName, val)


class ObjectFragmentMixin:
    pass

class GlobalObjectMixin:
    pass

class ExternalObjectMixin:
    pass

class DerivableObjectMixin:
    pass

class SubclassableObjectMixin:

    def get_abstract(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'abstract')
        return cast(bool, val)


class InheritingObjectMixin:

    def get_bases(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[objects.InheritingObject]':
        val = s_orm.get_field_value(self, schema, 'bases')
        return cast(objects.ObjectList[objects.InheritingObject], val)

    def get_ancestors(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[objects.InheritingObject]':
        val = s_orm.get_field_value(self, schema, 'ancestors')
        return cast(objects.ObjectList[objects.InheritingObject], val)

    def get_inherited_fields(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedSet[str]':
        val = s_orm.get_field_value(self, schema, 'inherited_fields')
        return cast(checked.FrozenCheckedSet[str], val)

    def get_is_derived(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'is_derived')
        return cast(bool, val)


class DerivableInheritingObjectMixin:
    pass