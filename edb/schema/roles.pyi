# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos

class Role(
    objects.GlobalObject,
    objects.InheritingObject,
    annos.AnnotationSubject
):

    def get_superuser(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_password(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_password_hash(
        self, schema: s_schema.Schema
    ) -> str: ...
