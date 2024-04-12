# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.edgeql import qltypes
from edb.schema import expr
from edb.schema import types

class Global(
    objects.QualifiedObject,
    annos.AnnotationSubject
):

    def get_target(
        self, schema: s_schema.Schema
    ) -> types.Type: ...

    def get_required(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_cardinality(
        self, schema: s_schema.Schema
    ) -> qltypes.SchemaCardinality: ...

    def get_expr(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_default(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_created_types(
        self, schema: s_schema.Schema
    ) -> objects.ObjectSet[types.Type]: ...
