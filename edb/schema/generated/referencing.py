# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm


class ReferencedObjectMixin:

    def get_owned(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'owned')
        return cast(bool, val)


class ReferencedInheritingObjectMixin:

    def get_declared_overloaded(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'declared_overloaded')
        return cast(bool, val)


class NamedReferencedInheritingObjectMixin:
    pass