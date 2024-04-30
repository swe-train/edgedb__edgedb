# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.edgeql import qltypes
from edb.schema import name
from edb.edgeql import ast
from edb.common import checked


class OperatorMixin:

    def get_operator_kind(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.OperatorKind':
        val = s_orm.get_field_value(self, schema, 'operator_kind')
        return cast(qltypes.OperatorKind, val)

    def get_language(
        self, schema: 's_schema.Schema'
    ) -> 'ast.Language':
        val = s_orm.get_field_value(self, schema, 'language')
        return cast(ast.Language, val)

    def get_from_operator(
        self, schema: 's_schema.Schema'
    ) -> 'checked.CheckedList[str]':
        val = s_orm.get_field_value(self, schema, 'from_operator')
        return cast(checked.CheckedList[str], val)

    def get_from_function(
        self, schema: 's_schema.Schema'
    ) -> 'checked.CheckedList[str]':
        val = s_orm.get_field_value(self, schema, 'from_function')
        return cast(checked.CheckedList[str], val)

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

    def get_code(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'code')
        return cast(str, val)

    def get_derivative_of(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        val = s_orm.get_field_value(self, schema, 'derivative_of')
        return cast(name.QualName, val)

    def get_commutator(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        val = s_orm.get_field_value(self, schema, 'commutator')
        return cast(name.QualName, val)

    def get_negator(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        val = s_orm.get_field_value(self, schema, 'negator')
        return cast(name.QualName, val)

    def get_recursive(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'recursive')
        return cast(bool, val)
