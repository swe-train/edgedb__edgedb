# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import name


class FutureBehaviorMixin:

    def get_name(
        self, schema: 's_schema.Schema'
    ) -> 'name.Name':
        val = s_orm.get_field_value(self, schema, 'name')
        return cast(name.Name, val)
