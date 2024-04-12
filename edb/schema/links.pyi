# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import sources
from edb.edgeql import qltypes
from edb.schema import pointers
from edb.schema import abc

class Link(sources.Source, pointers.Pointer, abc.Link):

    def get_on_target_delete(
        schema: s_schema.Schema
    ) -> qltypes.LinkTargetDeleteAction: ...

    def get_on_source_delete(
        schema: s_schema.Schema
    ) -> qltypes.LinkSourceDeleteAction: ...
