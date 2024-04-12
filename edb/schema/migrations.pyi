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
        schema: s_schema.Schema
    ) -> objects.ObjectList['Migration']: ...

    def get_message(
        schema: s_schema.Schema
    ) -> str: ...

    def get_generated_by(
        schema: s_schema.Schema
    ) -> str: ...

    def get_script(
        schema: s_schema.Schema
    ) -> str: ...
