"""Local model registry"""
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

from mlsteam_model_sdk.core.exceptions import ModelVersionNotFoundException, MultipleModelVersionsException
from mlsteam_model_sdk.utils.log import logger


class Registry:
    """Local model registry operator"""

    LOCAL_PUUID = '__local__'
    LOCAL_MUUID = '__local__'

    def __init__(self, config_dir: Path) -> None:
        """Initializes a local model registry operator.

        Args:
          config_dir: SDK configuration base directory
        """
        self._models_dir = config_dir / 'models'
        self._download_base_dir = self._models_dir / 'download'
        self._extract_base_dir = self._models_dir / 'extract'
        self._registry_file = self._models_dir / 'reg.json'

    def get_new_local_vuuid(self) -> str:
        """Generates a new local vuuid.

        NOTE: This method is not thread-safe.
        """
        while True:
            local_vuuid = 'local-' + str(uuid.uuid4())[:8]
            if self.get_model_version_info(vuuid=local_vuuid) is None:
                return local_vuuid

    def get_download_base_dir(self, create: bool = False) -> Path:
        """Gets base path to download model version files or packages."""
        if create:
            self._download_base_dir.mkdir(parents=True, exist_ok=True)
        return self._download_base_dir

    def get_download_file(self, vuuid: str, packaged: bool, encrypted: bool,
                          create_dir: bool = False) -> Path:
        """Gets path to save a downloaded model version file or package."""
        download_dir = self.get_download_base_dir(create=create_dir)
        if encrypted:
            download_name = f'{vuuid}-enc.mlarchive'
        elif packaged:
            download_name = f'{vuuid}.mlarchive'
        else:
            download_name = f'{vuuid}.zip'
        return download_dir / download_name

    def get_extract_base_dir(self, create: bool = False) -> Path:
        """Gets base path to extract non-encrypted model version packages."""
        if create:
            self._extract_base_dir.mkdir(parents=True, exist_ok=True)
        return self._extract_base_dir

    def get_extract_dir(self, vuuid: str, create_dir: bool = False) -> Path:
        """Gets path to extract a downloaded model version package."""
        extract_dir = self.get_extract_base_dir(create=create_dir) / vuuid
        if create_dir:
            extract_dir.mkdir(parents=True, exist_ok=True)
        return extract_dir

    def list_model_versions(self) -> Dict[str, dict]:
        """Gets information of model versions in local registry.

        Returns:
          model version dict [vuuid => model version info dict]
        """
        try:
            with self._registry_file.open('rt') as reg_file:
                reg_data = json.load(reg_file)
                return reg_data
        except FileNotFoundError as e:
            logger.warning(e)
            return {}

    def _find_model_version(self, reg_data: dict, version_name: str,
                            muuid: Optional[str] = None,
                            model_name: Optional[str] = None,
                            find_all: bool = False) -> Union[str, List[str]]:
        """Gets model version uuid(s) from model and version.

        Returns:
          model version uuid as a string when `find_all` is not set (default);
          otherwise, model version uuids as a list of strings

        Raises:
          ModelVersionNotFoundException: no matching model is found and `find_all` is not set
        """
        if muuid:
            def model_matcher(row): return row['muuid'] == muuid
        elif model_name:
            def model_matcher(row): return row['model_name'] == model_name
        else:
            raise ValueError('Neither muuid nor model_name is provided')

        matches = [row['vuuid'] for row in reg_data.values() if
                   row['version_name'] == version_name and model_matcher(row)]
        if find_all:
            return matches
        try:
            return matches[0]
        except IndexError:
            raise ModelVersionNotFoundException(muuid=muuid,
                                                model_name=model_name,
                                                version_name=version_name) from None

    def get_model_version_info(self,
                               vuuid: Optional[str] = None,
                               version_name: Optional[str] = None,
                               muuid: Optional[str] = None,
                               model_name: Optional[str] = None,
                               default_muuid: Optional[str] = None) -> Optional[dict]:
        """Gets information of a model version in local registry.

        A model version is specified in one of the following ways:
        - model version uuid (`vuuid`) alone
        - model (`muuid`, `model_name`, or `default_muuid`) combined with version (`version_name`)

        It returns the first matching model version.
        To get all matching model versions, call `list_model_versions()` instead.
        (It is possible to have multiple matches when a model version is specified by model name and version name.)

        Args:
          vuuid: model version uuid
          version_name: version name
          muuid: model uuid
          model_name: model name
          default_muuid: default model uuid

        Returns:
          model version info dict, or `None` when the model version is not found
        """
        try:
            with self._registry_file.open('rt') as reg_file:
                reg_data = json.load(reg_file)
                if not vuuid:
                    if not muuid and not model_name:
                        muuid = default_muuid
                    vuuid = self._find_model_version(
                        reg_data=reg_data, version_name=version_name,
                        muuid=muuid, model_name=model_name)
                return reg_data[vuuid]
        except (FileNotFoundError, KeyError, ModelVersionNotFoundException) as e:
            logger.warning(e)
            return None

    def set_model_version_info(self, puuid: str, muuid: str, model_name: str,
                               vuuid: str, version_name: str,
                               packaged: bool, encrypted: bool,
                               download_time: datetime):
        """Sets model version record in local registry."""
        if not self._registry_file.exists():
            with self._registry_file.open('wt') as reg_file:
                reg_file.write('{}')

        with self._registry_file.open('rt+') as reg_file:
            reg_data = json.load(reg_file)
            reg_data[vuuid] = {
                'puuid': puuid,
                'muuid': muuid,
                'model_name': model_name,
                'vuuid': vuuid,
                'version_name': version_name,
                'packaged': packaged,
                'encrypted': encrypted,
                'download_time': download_time.isoformat()
            }
            reg_file.seek(0)
            json.dump(reg_data, reg_file, indent=2)
            reg_file.write('\n')
            reg_file.truncate()

    def delete_model_version(self,
                             vuuid: Optional[str] = None,
                             version_name: Optional[str] = None,
                             muuid: Optional[str] = None,
                             model_name: Optional[str] = None,
                             default_muuid: Optional[str] = None,
                             delete_all: bool = False):
        """Deletes one or multiple model versions from local registry.

        A model version is specified in one of the following ways:
        - model version uuid (`vuuid`) alone
        - model (`muuid`, `model_name`, or `default_muuid`) combined with version (`version_name`)

        When `vuuid` is given, it will attempt to delete the associated files
        even when the local registry is broken.

        Args:
          vuuid: model version uuid
          version_name: version name
          muuid: model uuid
          model_name: model name
          default_muuid: default model uuid
          delete_all: delete all matching model versions

        Raises:
          MultipleModelVersionsException: there are multiple matching model versions and `delete_all` is not set
        """
        _vuuids = None
        try:
            with self._registry_file.open('rt+') as reg_file:
                reg_data = json.load(reg_file)
                if vuuid:
                    _vuuids = [vuuid]
                else:
                    if not muuid and not model_name:
                        muuid = default_muuid
                    _vuuids = self._find_model_version(
                        reg_data=reg_data, version_name=version_name,
                        muuid=muuid, model_name=model_name, find_all=True)

                if _vuuids:
                    if len(_vuuids) > 1 and not delete_all:
                        raise MultipleModelVersionsException(muuid=muuid, model_name=model_name,
                                                             version_name=version_name)
                    for mv in _vuuids:
                        del reg_data[mv]
                    reg_file.seek(0)
                    json.dump(reg_data, reg_file, indent=2)
                    reg_file.write('\n')
                    reg_file.truncate()  # file could be smaller; need to truncate remaining contents
        except (FileNotFoundError, KeyError, ModelVersionNotFoundException) as e:
            logger.warning(e)

        if _vuuids:
            for mv in _vuuids:
                self._delete_model_version_files(mv)

    def delete_model(self,
                     muuid: Optional[str] = None,
                     model_name: Optional[str] = None,
                     default_muuid: Optional[str] = None):
        """Deletes all model versions of a model from local registry.

        A model is specified by `muuid`, `model_name`, or `default_muuid`.

        Args:
          muuid: model uuid
          model_name: model name
          default_muuid: default model uuid
        """
        if muuid:
            def model_matcher(row): return row['muuid'] == muuid
        elif model_name:
            def model_matcher(row): return row['model_name'] == model_name
        elif default_muuid:
            def model_matcher(row): return row['muuid'] == default_muuid
        else:
            raise ValueError('Neither muuid nor model_name nor default_muuid is provided')

        with self._registry_file.open('rt+') as reg_file:
            reg_data = json.load(reg_file)
            for row in list(reg_data.values()):
                if model_matcher(row):
                    vuuid = row['vuuid']
                    self._delete_model_version_files(vuuid)
                    del reg_data[vuuid]
            reg_file.seek(0)
            json.dump(reg_data, reg_file, indent=2)
            reg_file.write('\n')
            reg_file.truncate()  # file could be smaller; need to truncate remaining contents

    def _delete_model_version_files(self, vuuid: str):
        """Deletes model version files.

        It attempts to delete associated files as many as possible
        even when errors occure.
        """
        if self._download_base_dir.exists():
            for _path in self._download_base_dir.iterdir():
                if (_path.is_file() and
                        _path.name.startswith(vuuid) and
                        _path.suffix in ('zip', 'mlarchive')):
                    try:
                        _path.unlink()
                    except (PermissionError,) as e:
                        logger.warning(e)

        extract_dir = self.get_extract_dir(vuuid, create_dir=False)
        if extract_dir.exists():
            self.__del_dir(extract_dir)

    @classmethod
    def __del_dir(cls, dir_path: Path):
        for _path in dir_path.iterdir():
            if _path.is_file():
                try:
                    _path.unlink()
                except (PermissionError,) as e:
                    logger.warning(e)
            else:
                cls.__del_dir(_path)

        try:
            dir_path.rmdir()
        except (PermissionError,) as e:
            logger.warn(e)
