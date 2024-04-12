# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
import uuid
from edb.common import span
from edb.schema import name
from edb.schema import abc
from edb.schema import objects
from edb.common import checked

class Object(
    abc.Object,
    objects.ObjectContainer
):

    def get_id(
        self, schema: s_schema.Schema
    ) -> uuid.UUID: ...

    def get_internal(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_sourcectx(
        self, schema: s_schema.Schema
    ) -> span.Span: ...

    def get_name(
        self, schema: s_schema.Schema
    ) -> name.Name: ...

    def get_builtin(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_computed_fields(
        self, schema: s_schema.Schema
    ) -> checked.FrozenCheckedSet[str]: ...

class QualifiedObject(
    objects.Object
):

    def get_name(
        self, schema: s_schema.Schema
    ) -> name.QualName: ...

class SubclassableObject(
    objects.Object
):

    def get_abstract(
        self, schema: s_schema.Schema
    ) -> bool: ...

class InheritingObject(
    objects.SubclassableObject
):

    def get_bases(
        self, schema: s_schema.Schema
    ) -> objects.ObjectList['InheritingObject']: ...

    def get_ancestors(
        self, schema: s_schema.Schema
    ) -> objects.ObjectList['InheritingObject']: ...

    def get_inherited_fields(
        self, schema: s_schema.Schema
    ) -> checked.FrozenCheckedSet[str]: ...

    def get_is_derived(
        self, schema: s_schema.Schema
    ) -> bool: ...
