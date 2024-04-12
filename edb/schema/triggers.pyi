# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import expr
from edb.edgeql import qltypes
from edb.schema import referencing

class Trigger(
    referencing.NamedReferencedInheritingObject,
    objects.InheritingObject
):

    def get_timing(
        self, schema: s_schema.Schema
    ) -> qltypes.TriggerTiming: ...

    def get_kinds(
        self, schema: s_schema.Schema
    ) -> objects.MultiPropSet[qltypes.TriggerKind]: ...

    def get_scope(
        self, schema: s_schema.Schema
    ) -> qltypes.TriggerScope: ...

    def get_expr(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_condition(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_subject(
        self, schema: s_schema.Schema
    ) -> objects.InheritingObject: ...

    def get_owned(
        self, schema: s_schema.Schema
    ) -> bool: ...
