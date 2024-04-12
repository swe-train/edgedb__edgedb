import types
import typing
import textwrap

from edb import schema
from edb.schema import objects as s_objects
from edb.common import typing_inspect

from edb.tools.edb import edbcommands


@edbcommands.command("gen-schema-types")
def main() -> None:

    for name, item in schema.__dict__.items():
        if not isinstance(item, types.ModuleType):
            continue

        gen_for_module(name, item)


def gen_for_module(mod_name: str, mod: types.ModuleType):

    schema_object_classes: typing.List[s_objects.Object] = []
    imports = set()

    for cls in mod.__dict__.values():
        if not (isinstance(cls, type) and issubclass(cls, s_objects.Object)):
            continue

        fa = '{}.{}_fields'.format(cls.__module__, cls.__name__)
        my_fields = getattr(cls, fa)

        if len(my_fields) == 0:
            continue

        for field in my_fields.values():
            collect_imports(field.type, imports)

        for base in cls.__bases__:
            collect_imports(base, imports)

        schema_object_classes.append(cls)
    if not schema_object_classes:
        return

    f = open(f'edb/schema/{mod_name}.pyi', 'w')

    f.write(
        textwrap.dedent(
            '''\
            # DO NOT EDIT. This file was generated with:
            #
            # $ gen-schema-types

            """Type definitions for generated methods on schema classes"""

            from edb import schema as s_schema
            '''
        )
    )
    for imp in imports:
        parts = imp.split('.')
        if len(parts) > 1:
            path = '.'.join(parts[0:-1])
            f.write(f'from {path} import {parts[-1]}\n')
        else:
            f.write(f'import {parts[-1]}\n')

    for cls in schema_object_classes:

        bases = ','.join(
            ('\n    ' + codegen_ty(base) for base in cls.__bases__)
        )

        f.write(f'\nclass {cls.__name__}({bases}\n):\n')

        fa = '{}.{}_fields'.format(cls.__module__, cls.__name__)
        my_fields = getattr(cls, fa)
        for field in my_fields.values():
            getter_name = f'get_{field.name}'

            ty = codegen_ty(field.type)

            f.write(
                '\n'
                f'    def {getter_name}(\n'
                f'        self, schema: s_schema.Schema\n'
                f'    ) -> {ty}: ...\n'
            )


def collect_imports(ty: type, imports: typing.Set[str]):
    if not isinstance(ty, type):
        return

    if ty.__module__ == 'builtins':
        return
    if typing_inspect.is_generic_type(ty):
        imports.add(ty.__base__.__module__)
        for arg in ty.orig_args:
            collect_imports(arg, imports)
        return
    imports.add(ty.__module__)


def codegen_ty(ty: type):
    if not isinstance(ty, type):
        return f'\'{ty}\''

    if ty.__module__ == 'builtins':
        return ty.__qualname__

    if typing_inspect.is_generic_type(ty):
        mod_name = ty.__base__.__module__.split('.')[-1]
        base_name = ty.__base__.__qualname__
        base_name = base_name.split('[')[0]
        base = f"{mod_name}.{base_name}"

        args = ', '.join((codegen_ty(arg) for arg in ty.orig_args))
        return f'{base}[{args}]'

    # base case
    mod_name = ty.__module__.split('.')[-1]
    return f"{mod_name}.{ty.__qualname__}"
