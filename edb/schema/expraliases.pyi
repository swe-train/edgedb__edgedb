# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import expr
from edb.schema import annos
from edb.schema import types

class Alias(
    objects.QualifiedObject,
    annos.AnnotationSubject
):

    def get_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_type(
        schema: s_schema.Schema
    ) -> types.Type: ...

    def get_created_types(
        schema: s_schema.Schema
    ) -> objects.ObjectSet[types.Type]: ...
