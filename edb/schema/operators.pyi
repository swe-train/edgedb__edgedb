# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import abc
from edb.edgeql import qltypes
from edb.schema import name
from edb.edgeql import ast
from edb.schema import functions
from edb.common import checked

class Operator(
    functions.CallableObject,
    functions.VolatilitySubject,
    abc.Operator
):

    def get_operator_kind(
        self, schema: s_schema.Schema
    ) -> qltypes.OperatorKind: ...

    def get_language(
        self, schema: s_schema.Schema
    ) -> ast.Language: ...

    def get_from_operator(
        self, schema: s_schema.Schema
    ) -> checked.CheckedList[str]: ...

    def get_from_function(
        self, schema: s_schema.Schema
    ) -> checked.CheckedList[str]: ...

    def get_from_expr(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_force_return_cast(
        self, schema: s_schema.Schema
    ) -> bool: ...

    def get_code(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_derivative_of(
        self, schema: s_schema.Schema
    ) -> name.QualName: ...

    def get_commutator(
        self, schema: s_schema.Schema
    ) -> name.QualName: ...

    def get_negator(
        self, schema: s_schema.Schema
    ) -> name.QualName: ...

    def get_recursive(
        self, schema: s_schema.Schema
    ) -> bool: ...
