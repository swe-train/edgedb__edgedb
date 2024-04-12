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

class Rewrite(
    referencing.NamedReferencedInheritingObject,
    objects.InheritingObject,
    annos.AnnotationSubject
):

    def get_kind(
        schema: s_schema.Schema
    ) -> qltypes.RewriteKind: ...

    def get_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_subject(
        schema: s_schema.Schema
    ) -> objects.InheritingObject: ...
