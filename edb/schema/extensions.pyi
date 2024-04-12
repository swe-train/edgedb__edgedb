# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.schema import extensions
from edb.common import checked
from edb.common import verutils

class ExtensionPackage(objects.GlobalObject, annos.AnnotationSubject):

    def get_version(
        schema: s_schema.Schema
    ) -> verutils.Version: ...

    def get_script(
        schema: s_schema.Schema
    ) -> str: ...

    def get_sql_extensions(
        schema: s_schema.Schema
    ) -> checked.FrozenCheckedSet[str]: ...

    def get_ext_module(
        schema: s_schema.Schema
    ) -> str: ...

    def get_dependencies(
        schema: s_schema.Schema
    ) -> checked.FrozenCheckedSet[str]: ...

class Extension(objects.Object):

    def get_package(
        schema: s_schema.Schema
    ) -> extensions.ExtensionPackage: ...

    def get_dependencies(
        schema: s_schema.Schema
    ) -> objects.ObjectList['Extension']: ...
