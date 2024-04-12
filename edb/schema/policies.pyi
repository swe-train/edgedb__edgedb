# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.edgeql import qltypes
from edb.schema import expr
from edb.schema import referencing

class AccessPolicy(
    referencing.NamedReferencedInheritingObject,
    objects.InheritingObject,
    annos.AnnotationSubject
):

    def get_condition(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_expr(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_action(
        self, schema: s_schema.Schema
    ) -> qltypes.AccessPolicyAction: ...

    def get_access_kinds(
        self, schema: s_schema.Schema
    ) -> objects.MultiPropSet[qltypes.AccessKind]: ...

    def get_subject(
        self, schema: s_schema.Schema
    ) -> objects.InheritingObject: ...

    def get_errmessage(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_owned(
        self, schema: s_schema.Schema
    ) -> bool: ...
