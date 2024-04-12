# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.edgeql import qltypes
from edb.schema import expr
from edb.schema import functions
from edb.schema import referencing
from edb.schema import indexes
from edb.common import checked

class Index(
    referencing.ReferencedInheritingObject,
    objects.InheritingObject,
    annos.AnnotationSubject
):

    def get_bases(
        schema: s_schema.Schema
    ) -> objects.ObjectList['Index']: ...

    def get_subject(
        schema: s_schema.Schema
    ) -> objects.Object: ...

    def get_params(
        schema: s_schema.Schema
    ) -> objects.ObjectList[functions.Parameter]: ...

    def get_code(
        schema: s_schema.Schema
    ) -> str: ...

    def get_kwargs(
        schema: s_schema.Schema
    ) -> checked.CheckedDict[str, expr.Expression]: ...

    def get_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_except_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_deferrability(
        schema: s_schema.Schema
    ) -> qltypes.IndexDeferrability: ...

    def get_deferred(
        schema: s_schema.Schema
    ) -> bool: ...

class IndexableSubject(
    objects.InheritingObject
):

    def get_indexes(
        schema: s_schema.Schema
    ) -> objects.ObjectIndexByFullname[indexes.Index]: ...
