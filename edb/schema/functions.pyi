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
        self, schema: s_schema.Schema
    ) -> int: ...

    def get_default(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_type(
        self, schema: s_schema.Schema
    ) -> types.Type: ...

    def get_typemod(
        self, schema: s_schema.Schema
    ) -> qltypes.TypeModifier: ...

    def get_kind(
        self, schema: s_schema.Schema
    ) -> qltypes.ParameterKind: ...

class VolatilitySubject(
    objects.Object
):

    def get_volatility(
        self, schema: s_schema.Schema
    ) -> qltypes.Volatility: ...

class CallableObject(
    objects.QualifiedObject,
    annos.AnnotationSubject,
    functions.CallableLike
):

    def get_params(
        self, schema: s_schema.Schema
    ) -> objects.ObjectList[functions.Parameter]: ...

    def get_return_type(
        self, schema: s_schema.Schema
    ) -> types.Type: ...

    def get_return_typemod(
        self, schema: s_schema.Schema
    ) -> qltypes.TypeModifier: ...

    def get_abstract(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_impl_is_strict(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_prefer_subquery_args(
        self, schema: s_schema.Schema
    ) -> bool: ...

class Function(
    functions.CallableObject,
    functions.VolatilitySubject,
    abc.Function
):

    def get_used_globals(
        self, schema: s_schema.Schema
    ) -> objects.ObjectSet[globals.Global]: ...

    def get_backend_name(
        self, schema: s_schema.Schema
    ) -> uuid.UUID: ...

    def get_code(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_nativecode(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_language(
        self, schema: s_schema.Schema
    ) -> ast.Language: ...

    def get_reflected_language(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_from_function(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_from_expr(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_force_return_cast(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_sql_func_has_out_params(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_error_on_null_result(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_preserves_optionality(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_preserves_upper_cardinality(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_initial_value(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_has_dml(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_fallback(
        self, schema: s_schema.Schema
    ) -> bool: ...
