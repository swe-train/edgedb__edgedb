# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
import uuid
from edb.edgeql import qltypes
from edb.edgeql import ast
from edb.schema import expr
from edb.schema import functions
from edb.schema import types
from edb.schema import globals


class ParameterMixin:

    def get_num(
        self, schema: 's_schema.Schema'
    ) -> 'int':
        val = s_orm.get_field_value(self, schema, 'num')
        return cast(int, val)

    def get_default(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'default')
        return cast(expr.Expression, val)

    def get_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'type')
        return cast(types.Type, val)

    def get_typemod(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.TypeModifier':
        val = s_orm.get_field_value(self, schema, 'typemod')
        return cast(qltypes.TypeModifier, val)

    def get_kind(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.ParameterKind':
        val = s_orm.get_field_value(self, schema, 'kind')
        return cast(qltypes.ParameterKind, val)


class VolatilitySubjectMixin:

    def get_volatility(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.Volatility':
        val = s_orm.get_field_value(self, schema, 'volatility')
        return cast(qltypes.Volatility, val)


class CallableObjectMixin:

    def get_params(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[functions.Parameter]':
        val = s_orm.get_field_value(self, schema, 'params')
        return cast(objects.ObjectList[functions.Parameter], val)

    def get_return_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        val = s_orm.get_field_value(self, schema, 'return_type')
        return cast(types.Type, val)

    def get_return_typemod(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.TypeModifier':
        val = s_orm.get_field_value(self, schema, 'return_typemod')
        return cast(qltypes.TypeModifier, val)

    def get_abstract(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'abstract')
        return cast(bool, val)

    def get_impl_is_strict(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'impl_is_strict')
        return cast(bool, val)

    def get_prefer_subquery_args(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'prefer_subquery_args')
        return cast(bool, val)


class FunctionMixin:

    def get_used_globals(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[globals.Global]':
        val = s_orm.get_field_value(self, schema, 'used_globals')
        return cast(objects.ObjectSet[globals.Global], val)

    def get_backend_name(
        self, schema: 's_schema.Schema'
    ) -> 'uuid.UUID':
        val = s_orm.get_field_value(self, schema, 'backend_name')
        return cast(uuid.UUID, val)

    def get_code(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'code')
        return cast(str, val)

    def get_nativecode(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'nativecode')
        return cast(expr.Expression, val)

    def get_language(
        self, schema: 's_schema.Schema'
    ) -> 'ast.Language':
        val = s_orm.get_field_value(self, schema, 'language')
        return cast(ast.Language, val)

    def get_reflected_language(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'reflected_language')
        return cast(str, val)

    def get_from_function(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'from_function')
        return cast(str, val)

    def get_from_expr(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'from_expr')
        return cast(bool, val)

    def get_force_return_cast(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'force_return_cast')
        return cast(bool, val)

    def get_sql_func_has_out_params(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'sql_func_has_out_params')
        return cast(bool, val)

    def get_error_on_null_result(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'error_on_null_result')
        return cast(str, val)

    def get_preserves_optionality(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'preserves_optionality')
        return cast(bool, val)

    def get_preserves_upper_cardinality(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'preserves_upper_cardinality')
        return cast(bool, val)

    def get_initial_value(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'initial_value')
        return cast(expr.Expression, val)

    def get_has_dml(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'has_dml')
        return cast(bool, val)

    def get_fallback(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'fallback')
        return cast(bool, val)
