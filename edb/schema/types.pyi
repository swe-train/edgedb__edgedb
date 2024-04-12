# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import abc
from edb.schema import annos
from edb.schema import expr
from edb.schema import types
from edb.common import checked

class Type(
    objects.SubclassableObject,
    annos.AnnotationSubject,
    abc.Type
):

    def get_expr(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_expr_type(
        self, schema: s_schema.Schema
    ) -> types.ExprType: ...

    def get_from_alias(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_from_global(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_alias_is_persistent(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_rptr(
        self, schema: s_schema.Schema
    ) -> objects.Object: ...

    def get_backend_id(
        self, schema: s_schema.Schema
    ) -> int: ...

    def get_transient(
        self, schema: s_schema.Schema
    ) -> bool: ...

class Collection(
    types.Type,
    abc.Collection
):

    def get_is_persistent(
        self, schema: s_schema.Schema
    ) -> bool: ...

class Array(
    types.Collection,
    abc.Array
):

    def get_element_type(
        self, schema: s_schema.Schema
    ) -> types.Type: ...

    def get_dimensions(
        self, schema: s_schema.Schema
    ) -> checked.FrozenCheckedList[int]: ...

class Tuple(
    types.Collection,
    abc.Tuple
):

    def get_named(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_element_types(
        self, schema: s_schema.Schema
    ) -> objects.ObjectDict[str, types.Type]: ...

class Range(
    types.Collection,
    abc.Range
):

    def get_element_type(
        self, schema: s_schema.Schema
    ) -> types.Type: ...

class MultiRange(
    types.Collection,
    abc.MultiRange
):

    def get_element_type(
        self, schema: s_schema.Schema
    ) -> types.Type: ...
