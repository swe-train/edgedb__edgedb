# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.edgeql import qltypes
from edb.schema import rewrites
from edb.schema import abc
from edb.schema import expr
from edb.schema import types
from edb.schema import referencing
from edb.schema import constraints

class Pointer(
    referencing.NamedReferencedInheritingObject,
    constraints.ConsistencySubject,
    annos.AnnotationSubject,
    abc.Pointer
):

    def get_source(
        schema: s_schema.Schema
    ) -> objects.InheritingObject: ...

    def get_target(
        schema: s_schema.Schema
    ) -> types.Type: ...

    def get_required(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_readonly(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_secret(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_protected(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_computable(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_from_alias(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_defined_here(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_default(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_cardinality(
        schema: s_schema.Schema
    ) -> qltypes.SchemaCardinality: ...

    def get_union_of(
        schema: s_schema.Schema
    ) -> objects.ObjectSet['Pointer']: ...

    def get_intersection_of(
        schema: s_schema.Schema
    ) -> objects.ObjectSet['Pointer']: ...

    def get_computed_link_alias_is_backward(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_computed_link_alias(
        schema: s_schema.Schema
    ) -> objects.Object: ...

    def get_rewrites(
        schema: s_schema.Schema
    ) -> objects.ObjectIndexByUnqualifiedName[rewrites.Rewrite]: ...
