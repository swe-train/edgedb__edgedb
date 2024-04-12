# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import abc
from edb.schema import expr
from edb.schema import types
from edb.common import checked
from edb.schema import constraints

class ScalarType(
    types.InheritingType,
    constraints.ConsistencySubject,
    abc.ScalarType
):

    def get_default(
        self, schema: s_schema.Schema
    ) -> expr.Expression: ...

    def get_enum_values(
        self, schema: s_schema.Schema
    ) -> checked.FrozenCheckedList[str]: ...

    def get_sql_type(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_sql_type_scheme(
        self, schema: s_schema.Schema
    ) -> str: ...

    def get_num_params(
        self, schema: s_schema.Schema
    ) -> int: ...

    def get_arg_values(
        self, schema: s_schema.Schema
    ) -> checked.FrozenCheckedList[str]: ...
