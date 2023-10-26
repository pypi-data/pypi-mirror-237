import sys

import click
import texttable

from mlsteam_model_sdk.core.exceptions import MultipleModelVersionsException
from mlsteam_model_sdk.core.registry import Registry
from mlsteam_model_sdk.utils.config import get_config_path


MV_COLS = ['muuid', 'model_name', 'vuuid', 'version_name', 'puuid', 'packaged', 'encrypted', 'download_time']


@click.group(help='model version operations')
def mv():
    pass


@mv.command(name='list-local',  help='list local model versions')
def list_local():
    reg = Registry(get_config_path(check=True).parent)
    mvs = reg.list_model_versions()

    table = texttable.Texttable(max_width=0)
    table.set_deco(texttable.Texttable.HEADER)
    table.header(MV_COLS)
    for _mv in mvs.values():
        table.add_row([_mv[c] for c in MV_COLS])
    click.echo(table.draw())


@mv.command(name='get-local', help='get local model version info')
@click.option('--vuuid', help='version uuid')
@click.option('--version_name', help='version name')
@click.option('--muuid', help='model uuid')
@click.option('--model_name', help='model name')
def get_local(vuuid, version_name, muuid, model_name):
    reg = Registry(get_config_path(check=True).parent)
    _mv = reg.get_model_version_info(vuuid=vuuid,
                                     version_name=version_name,
                                     muuid=muuid,
                                     model_name=model_name)
    if _mv is None:
        click.echo('Model version not found', err=True)
        sys.exit(1)

    table = texttable.Texttable(max_width=0)
    table.set_deco(texttable.Texttable.HEADER)
    table.header(MV_COLS)
    table.add_row([_mv[c] for c in MV_COLS])
    click.echo(table.draw())


@mv.command(name='import-local', help='import a model version package')
@click.option('-f', '--pkg_file', required=True,
              type=click.Path(exists=True, file_okay=True, readable=True, resolve_path=True),
              help='model version package file')
@click.option('-k', '--enckey_file',
              type=click.Path(exists=True, file_okay=True, readable=True, resolve_path=True),
              help='model version package encryption key file (required for encrypted packages)')
@click.option('--model_name', help='model name to register (a default value is used if not given)')
@click.option('--version_name', help='version name to register (a default value is used if not given)')
def import_local(pkg_file, enckey_file, model_name, version_name):
    from mlsteam_model_sdk.sdk.model import Model
    model_sdk = Model(offline=True)
    model_sdk.import_model_version(mv_package_file=pkg_file,
                                   enckey_file=enckey_file,
                                   model_name=model_name,
                                   version_name=version_name,
                                   logging=True)


@mv.command(name='del-local', help='delete a model version package')
@click.option('--vuuid', help='version uuid')
@click.option('--version_name', help='version name')
@click.option('--muuid', help='model uuid')
@click.option('--model_name', help='model name')
@click.option('--del_all', is_flag=True, default=False,
              help='delete all matching model versions; '
              'by default, it reports an error when multiple matching model versions are found')
def del_local(vuuid, version_name, muuid, model_name, del_all):
    from mlsteam_model_sdk.sdk.model import Model
    model_sdk = Model(offline=True)
    try:
        model_sdk.delete_model_version(vuuid=vuuid,
                                       version_name=version_name,
                                       muuid=muuid,
                                       model_name=model_name,
                                       delete_all=del_all)
    except MultipleModelVersionsException as e:
        click.echo(str(e), err=True)
        click.echo('To delete all matching model versions, add `--del_all`.')
        sys.exit(1)


@mv.command(name='del-all-local', help='delete all model version packages of a model')
@click.option('--muuid', help='model uuid')
@click.option('--model_name', help='model name')
@click.option('--force', is_flag=True, help='force delete model when a local-import muuid is given')
def del_all_local(muuid, model_name, force):
    from mlsteam_model_sdk.sdk.model import Model
    if muuid == Registry.LOCAL_MUUID and not force:
        click.echo('Deleting a locally-imported model by `muuid` '
                   'will delete all other locally-imported models as well. '
                   'If it is intended, add `--force`.', err=True)
        sys.exit(1)
    model_sdk = Model(offline=True)
    model_sdk.delete_model(muuid=muuid,
                           model_name=model_name)
