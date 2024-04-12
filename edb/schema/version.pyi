# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
import uuid
from edb.schema import objects

class BaseSchemaVersion(
    objects.Object
):

    def get_version(
        self, schema: s_schema.Schema
    ) -> uuid.UUID: ...
