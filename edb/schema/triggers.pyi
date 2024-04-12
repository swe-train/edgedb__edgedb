# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import expr
from edb.edgeql import qltypes
from edb.schema import referencing

class Trigger(referencing.NamedReferencedInheritingObject, objects.InheritingObject):

    def get_timing(
        schema: s_schema.Schema
    ) -> qltypes.TriggerTiming: ...

    def get_kinds(
        schema: s_schema.Schema
    ) -> objects.MultiPropSet[qltypes.TriggerKind]: ...

    def get_scope(
        schema: s_schema.Schema
    ) -> qltypes.TriggerScope: ...

    def get_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_condition(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_subject(
        schema: s_schema.Schema
    ) -> objects.InheritingObject: ...

    def get_owned(
        schema: s_schema.Schema
    ) -> bool: ...
