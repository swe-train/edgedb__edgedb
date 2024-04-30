# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.schema import migrations


class MigrationMixin:

    def get_parents(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[migrations.Migration]':
        val = s_orm.get_field_value(self, schema, 'parents')
        return cast(objects.ObjectList[migrations.Migration], val)

    def get_message(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'message')
        return cast(str, val)

    def get_generated_by(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'generated_by')
        return cast(str, val)

    def get_script(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'script')
        return cast(str, val)
