# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import referencing

class ReferencedObject(
    objects.DerivableObject
):

    def get_owned(
        self, schema: s_schema.Schema
    ) -> bool: ...

class ReferencedInheritingObject(
    objects.DerivableInheritingObject,
    referencing.ReferencedObject
):

    def get_declared_overloaded(
        self, schema: s_schema.Schema
    ) -> bool: ...
