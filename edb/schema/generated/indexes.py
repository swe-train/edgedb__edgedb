# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.edgeql import qltypes
from edb.schema import indexes
from edb.common import checked
from edb.schema import expr
from edb.schema import functions


class IndexMixin:

    def get_bases(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[indexes.Index]':
        val = s_orm.get_field_value(self, schema, 'bases')
        return cast(objects.ObjectList[indexes.Index], val)

    def get_subject(
        self, schema: 's_schema.Schema'
    ) -> 'objects.Object':
        val = s_orm.get_field_value(self, schema, 'subject')
        return cast(objects.Object, val)

    def get_params(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[functions.Parameter]':
        val = s_orm.get_field_value(self, schema, 'params')
        return cast(objects.ObjectList[functions.Parameter], val)

    def get_code(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'code')
        return cast(str, val)

    def get_kwargs(
        self, schema: 's_schema.Schema'
    ) -> 'checked.CheckedDict[str, expr.Expression]':
        val = s_orm.get_field_value(self, schema, 'kwargs')
        return cast(checked.CheckedDict[str, expr.Expression], val)

    def get_type_args(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[objects.Object]':
        val = s_orm.get_field_value(self, schema, 'type_args')
        return cast(objects.ObjectList[objects.Object], val)

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'expr')
        return cast(expr.Expression, val)

    def get_except_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        val = s_orm.get_field_value(self, schema, 'except_expr')
        return cast(expr.Expression, val)

    def get_deferrability(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.IndexDeferrability':
        val = s_orm.get_field_value(self, schema, 'deferrability')
        return cast(qltypes.IndexDeferrability, val)

    def get_deferred(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'deferred')
        return cast(bool, val)


class IndexableSubjectMixin:

    def get_indexes(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectIndexByFullname[indexes.Index]':
        val = s_orm.get_field_value(self, schema, 'indexes')
        return cast(objects.ObjectIndexByFullname[indexes.Index], val)
