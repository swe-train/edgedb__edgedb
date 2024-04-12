# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import pointers
from edb.schema import indexes

class Source(objects.QualifiedObject, indexes.IndexableSubject, objects.Object):

    def get_pointers(
        schema: s_schema.Schema
    ) -> objects.ObjectIndexByUnqualifiedName[pointers.Pointer]: ...
