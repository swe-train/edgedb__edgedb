# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import name

class FutureBehavior(
    objects.Object
):

    def get_name(
        self, schema: s_schema.Schema
    ) -> name.Name: ...
