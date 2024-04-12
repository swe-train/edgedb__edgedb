# DO NOT EDIT. This file was generated with:
#
# $ gen-schema-types

"""Type definitions for generated methods on schema classes"""

from edb import schema as s_schema
from edb.schema import objects
from edb.schema import referencing
from edb.schema import annos

class AnnotationValue(
    referencing.ReferencedInheritingObject
):

    def get_subject(
        self, schema: s_schema.Schema
    ) -> objects.Object: ...

    def get_annotation(
        self, schema: s_schema.Schema
    ) -> annos.Annotation: ...

    def get_value(
        self, schema: s_schema.Schema
    ) -> str: ...

class AnnotationSubject(
    objects.Object
):

    def get_annotations(
        self, schema: s_schema.Schema
    ) -> objects.ObjectIndexByShortname[annos.AnnotationValue]: ...

class Annotation(
    objects.QualifiedObject,
    objects.InheritingObject,
    annos.AnnotationSubject
):

    def get_inheritable(
        self, schema: s_schema.Schema
    ) -> bool: ...
