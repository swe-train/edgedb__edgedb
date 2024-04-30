# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.schema import annos


class AnnotationValueMixin:

    def get_subject(
        self, schema: 's_schema.Schema'
    ) -> 'objects.Object':
        val = s_orm.get_field_value(self, schema, 'subject')
        return cast(objects.Object, val)

    def get_annotation(
        self, schema: 's_schema.Schema'
    ) -> 'annos.Annotation':
        val = s_orm.get_field_value(self, schema, 'annotation')
        return cast(annos.Annotation, val)

    def get_value(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        val = s_orm.get_field_value(self, schema, 'value')
        return cast(str, val)


class AnnotationSubjectMixin:

    def get_annotations(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectIndexByShortname[annos.AnnotationValue]':
        val = s_orm.get_field_value(self, schema, 'annotations')
        return cast(objects.ObjectIndexByShortname[annos.AnnotationValue], val)


class AnnotationMixin:

    def get_inheritable(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        val = s_orm.get_field_value(self, schema, 'inheritable')
        return cast(bool, val)
