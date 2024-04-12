# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import annos
from edb.edgeql import qltypes
import uuid
from edb.edgeql import ast
from edb.schema import abc
from edb.schema import expr
from edb.schema import functions
from edb.schema import types
from edb.schema import globals

class Parameter(
    objects.ObjectFragment,
    objects.Object,
    functions.ParameterLike
):

    def get_num(
        schema: s_schema.Schema
    ) -> int: ...

    def get_default(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_type(
        schema: s_schema.Schema
    ) -> types.Type: ...

    def get_typemod(
        schema: s_schema.Schema
    ) -> qltypes.TypeModifier: ...

    def get_kind(
        schema: s_schema.Schema
    ) -> qltypes.ParameterKind: ...

class VolatilitySubject(
    objects.Object
):

    def get_volatility(
        schema: s_schema.Schema
    ) -> qltypes.Volatility: ...

class CallableObject(
    objects.QualifiedObject,
    annos.AnnotationSubject,
    functions.CallableLike
):

    def get_params(
        schema: s_schema.Schema
    ) -> objects.ObjectList[functions.Parameter]: ...

    def get_return_type(
        schema: s_schema.Schema
    ) -> types.Type: ...

    def get_return_typemod(
        schema: s_schema.Schema
    ) -> qltypes.TypeModifier: ...

    def get_abstract(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_impl_is_strict(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_prefer_subquery_args(
        schema: s_schema.Schema
    ) -> bool: ...

class Function(
    functions.CallableObject,
    functions.VolatilitySubject,
    abc.Function
):

    def get_used_globals(
        schema: s_schema.Schema
    ) -> objects.ObjectSet[globals.Global]: ...

    def get_backend_name(
        schema: s_schema.Schema
    ) -> uuid.UUID: ...

    def get_code(
        schema: s_schema.Schema
    ) -> str: ...

    def get_nativecode(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_language(
        schema: s_schema.Schema
    ) -> ast.Language: ...

    def get_reflected_language(
        schema: s_schema.Schema
    ) -> str: ...

    def get_from_function(
        schema: s_schema.Schema
    ) -> str: ...

    def get_from_expr(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_force_return_cast(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_sql_func_has_out_params(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_error_on_null_result(
        schema: s_schema.Schema
    ) -> str: ...

    def get_preserves_optionality(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_preserves_upper_cardinality(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_initial_value(
        schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_has_dml(
        schema: s_schema.Schema
    ) -> bool: ...

    def get_fallback(
        schema: s_schema.Schema
    ) -> bool: ...
