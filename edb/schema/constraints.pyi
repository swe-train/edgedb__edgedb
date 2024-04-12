# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import abc
from edb.schema import annos
from edb.schema import expr
from edb.schema import functions
from edb.schema import referencing
from edb.common import checked
from edb.schema import constraints

class Constraint(
    referencing.ReferencedInheritingObject,
    functions.CallableObject,
    abc.Constraint
):

    def get_params(
        schema: s_schema.Schema
    ) -> objects.ObjectList[functions.Parameter]: ...

    def get_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_subjectexpr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_finalexpr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_except_expr(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_subject(
        schema: s_schema.Schema
    ) -> objects.Object: ...

    def get_args(
        schema: s_schema.Schema
    ) -> checked.FrozenCheckedList[expr.Expression]: ...

    def get_delegated(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_errmessage(
        schema: s_schema.Schema
    ) -> str: ...

    def get_is_aggregate(
        schema: s_schema.Schema
    ) -> bool: ...

class ConsistencySubject(
    objects.QualifiedObject,
    objects.InheritingObject,
    annos.AnnotationSubject
):

    def get_constraints(
        schema: s_schema.Schema
    ) -> constraints.ObjectIndexByConstraintName[constraints.Constraint]: ...
