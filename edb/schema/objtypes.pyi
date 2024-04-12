# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.schema import abc
from edb.schema import objtypes
from edb.schema import types
from edb.schema import sources
from edb.schema import triggers
from edb.schema import constraints
from edb.schema import policies

class ObjectTypeRefMixin(
    objects.Object
):

    def get_access_policies(
        schema: s_schema.Schema
    ) -> objects.ObjectIndexByUnqualifiedName[policies.AccessPolicy]: ...

    def get_triggers(
        schema: s_schema.Schema
    ) -> objects.ObjectIndexByUnqualifiedName[triggers.Trigger]: ...

class ObjectType(
    sources.Source,
    constraints.ConsistencySubject,
    types.InheritingType,
    objects.InheritingObject,
    types.Type,
    annos.AnnotationSubject,
    objtypes.ObjectTypeRefMixin,
    abc.ObjectType
):

    def get_union_of(
        schema: s_schema.Schema
    ) -> objects.ObjectSet['ObjectType']: ...

    def get_intersection_of(
        schema: s_schema.Schema
    ) -> objects.ObjectSet['ObjectType']: ...

    def get_is_opaque_union(
        schema: s_schema.Schema
    ) -> bool: ...
