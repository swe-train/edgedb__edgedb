# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import abc

class Migration(
    objects.Object,
    abc.Migration
):

    def get_parents(
        self, schema: s_schema.Schema
    ) -> objects.ObjectList['Migration']: ...

    def get_message(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_generated_by(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_script(
        self, schema: s_schema.Schema
    ) -> str: ...
