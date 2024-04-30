# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.schema import extensions
from edb.common import checked
from edb.common import verutils


class ExtensionPackageMixin:

    def get_version(
        self, schema: 's_schema.Schema'
    ) -> 'verutils.Version':
        val = s_orm.get_field_value(self, schema, 'version')
        return cast(verutils.Version, val)

    def get_script(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'script')
        return cast(str, val)

    def get_sql_extensions(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedSet[str]':
        val = s_orm.get_field_value(self, schema, 'sql_extensions')
        return cast(checked.FrozenCheckedSet[str], val)

    def get_ext_module(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'ext_module')
        return cast(str, val)

    def get_dependencies(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedSet[str]':
        val = s_orm.get_field_value(self, schema, 'dependencies')
        return cast(checked.FrozenCheckedSet[str], val)


class ExtensionMixin:

    def get_package(
        self, schema: 's_schema.Schema'
    ) -> 'extensions.ExtensionPackage':
        val = s_orm.get_field_value(self, schema, 'package')
        return cast(extensions.ExtensionPackage, val)

    def get_dependencies(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[extensions.Extension]':
        val = s_orm.get_field_value(self, schema, 'dependencies')
        return cast(objects.ObjectList[extensions.Extension], val)
