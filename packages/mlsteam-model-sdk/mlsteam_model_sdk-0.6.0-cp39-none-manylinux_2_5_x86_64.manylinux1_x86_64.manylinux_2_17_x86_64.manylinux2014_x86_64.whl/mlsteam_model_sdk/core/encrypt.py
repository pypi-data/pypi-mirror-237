import abc
import enum
from typing import BinaryIO, Callable, Optional

from pythemis.scell import SCellSeal
from pythemis.smessage import SMessage
from pythemis.skeygen import GenerateKeyPair, GenerateSymmetricKey, KEY_PAIR_TYPE

from mlsteam_model_sdk.utils.license import get_platform_id


class TrunkIO:

    class Mode(enum.Enum):
        BYTES = 1
        LEN_BYTES = 2

    def __init__(self, trunk_size: int, len_size: int, len_byteorder: str) -> None:
        self.trunk_size = trunk_size
        self.len_size = len_size
        self.len_byteorder = len_byteorder

    def read_file_trunk(self, src_file: BinaryIO) -> bytes:
        trunk_len = int.from_bytes(src_file.read(self.len_size), byteorder=self.len_byteorder)
        trunk = src_file.read(trunk_len)
        return trunk

    def write_file_trunk(self, dst_file: BinaryIO, trunk: bytes) -> None:
        dst_file.write(len(trunk).to_bytes(length=self.len_size, byteorder=self.len_byteorder))
        dst_file.write(trunk)

    def proc_file_in_trunks(self, src_file: BinaryIO, dst_file: BinaryIO,
                            read_mode: 'TrunkIO.Mode', write_mode: 'TrunkIO.Mode',
                            proc_func: Callable[[bytes], bytes]) -> None:
        while True:
            if read_mode == self.Mode.BYTES:
                trunk = src_file.read(self.trunk_size)
            else:
                trunk = self.read_file_trunk(src_file)
            if len(trunk) == 0:
                return
            proc_trunk = proc_func(trunk)
            if write_mode == self.Mode.BYTES:
                dst_file.write(proc_trunk)
            else:
                self.write_file_trunk(dst_file=dst_file, trunk=proc_trunk)


class ModelSealerBase(metaclass=abc.ABCMeta):
    TRUNK_SIZE = 10 * 1024 * 1024  # 10 MB
    trunk_io = TrunkIO(trunk_size=TRUNK_SIZE, len_size=8, len_byteorder='little')

    @abc.abstractmethod
    def _get_sealer(self) -> SCellSeal:
        ...

    def encrypt(self, data: bytes) -> bytes:
        sealer = self._get_sealer()
        return sealer.encrypt(data)

    def decrypt(self, data: bytes) -> bytes:
        sealer = self._get_sealer()
        return sealer.decrypt(data)

    def encrypt_file_trunk(self, dst_file: BinaryIO, trunk: bytes) -> None:
        """Encrypts a trunk and saves it into file.

        NOTE: The file is not closed by this method.

        Args:
          dst_file: destination file, should be opened in writable binary mode and positioned to the starting location
        """
        trunk_enc = self.encrypt(trunk)
        self.trunk_io.write_file_trunk(dst_file=dst_file, trunk=trunk_enc)

    def decrypt_file_trunk(self, src_file: BinaryIO) -> bytes:
        """Decrypts a trunk from file.

        NOTE: The file is not closed by this method.

        Args:
          src_file: source file, should be opened in readable binary mode and positioned to the starting location
        """
        trunc_enc = self.trunk_io.read_file_trunk(src_file)
        return self.decrypt(trunc_enc)

    def encrypt_file_in_trunks(self, src_file: BinaryIO, dst_file: BinaryIO):
        """Encrypts a potentially large file in trunks.

        NOTE: The files are not closed by this method.

        Args:
          src_file: source file, should be opened in readable binary mode and positioned to the starting location
          dst_file: destination file, should be opened in writable binary mode and positioned to the starting location
        """
        self.trunk_io.proc_file_in_trunks(src_file=src_file, dst_file=dst_file,
                                          read_mode=TrunkIO.Mode.BYTES, write_mode=TrunkIO.Mode.LEN_BYTES,
                                          proc_func=self._get_sealer().encrypt)

    def decrypt_file_from_trunks(self, src_file: BinaryIO, dst_file: BinaryIO):
        """Decrypts a potentially large file from trunks.

        NOTE: The files are not closed by this method.

        Args:
          src_file: source file, should be opened in readable binary mode and positioned to the starting location
          dst_file: destination file, should be opened in writable binary mode and positioned to the starting location
        """
        self.trunk_io.proc_file_in_trunks(src_file=src_file, dst_file=dst_file,
                                          read_mode=TrunkIO.Mode.LEN_BYTES, write_mode=TrunkIO.Mode.BYTES,
                                          proc_func=self._get_sealer().decrypt)


class ClientStorageModelSealer(ModelSealerBase):
    _sealer = None
    __MODEL_CLIENT_STORAGE_DEK_SEED = 'ml:storage-client~'

    def _get_sealer(self) -> SCellSeal:
        if self._sealer is None:
            ph = self.__MODEL_CLIENT_STORAGE_DEK_SEED + '//' + get_platform_id()
            self._sealer = SCellSeal(passphrase=ph)
        return self._sealer


class ClientServerExchSealer(ModelSealerBase):
    _sealer = None
    __MODEL_CLIENT_SERVER_EXCH_DEK_SEED = 'ml-Client-Server-##$##-enc'

    def _get_sealer(self) -> SCellSeal:
        if self._sealer is None:
            ph = self.__MODEL_CLIENT_SERVER_EXCH_DEK_SEED
            self._sealer = SCellSeal(passphrase=ph)
        return self._sealer


class ModelImportSealer(ModelSealerBase):

    class EncKeyType(enum.Enum):
        auto = 1
        custom = 2

    ENCKEY_TYPE_LEN = 1
    ENCKEY_SIZE_LEN = 2
    IO_BYTEORDER = 'little'

    def __init__(self,
                 enckey_type: Optional[EncKeyType] = None,
                 enckey: Optional[bytes] = None,
                 custom_encpass: Optional[str] = None) -> None:
        super().__init__()

        self.__enckey_type = enckey_type
        self.__custom_encpass = custom_encpass
        self.__enckey: Optional[bytes] = None

        if enckey_type is None:
            self.__sealer = None
        elif enckey_type == self.EncKeyType.auto:
            self.__enckey = GenerateSymmetricKey() if enckey is None else enckey
            self.__sealer = SCellSeal(key=self.__enckey)
        elif enckey_type == self.EncKeyType.custom:
            if not custom_encpass:
                raise ValueError('Missing custom_encpass')
            self.__sealer = SCellSeal(passphrase=self.__custom_encpass)
        else:
            raise ValueError('Invalid enckey_type')

    @classmethod
    def from_bytes(cls, src: BinaryIO) -> 'ModelImportSealer':
        enckey_type_val = int.from_bytes(
            src.read(cls.ENCKEY_TYPE_LEN), byteorder=cls.IO_BYTEORDER)
        enckey_type = cls.EncKeyType(enckey_type_val)
        enckey_bytes = cls._read_enckey(src)

        if enckey_type == cls.EncKeyType.auto:
            sealer = ModelImportSealer(enckey_type=enckey_type,
                                       enckey=enckey_bytes)
        elif enckey_type == cls.EncKeyType.custom:
            sealer = ModelImportSealer(enckey_type=enckey_type,
                                       custom_encpass=enckey_bytes.decode())
        else:
            raise ValueError('Invalid enckey_type')

        return sealer

    def to_bytes(self, dst: BinaryIO):
        dst.write(int(self.__enckey_type.value).to_bytes(
            length=self.ENCKEY_TYPE_LEN, byteorder=self.IO_BYTEORDER))

        if self.__enckey_type == self.EncKeyType.auto:
            self._write_enckey(dst, self.__enckey)
        elif self.__enckey_type == self.EncKeyType.custom:
            self._write_enckey(dst, self.__custom_encpass.encode())

    @classmethod
    def _read_enckey(cls, src: BinaryIO) -> bytes:
        data_size = int.from_bytes(
            src.read(cls.ENCKEY_SIZE_LEN), byteorder=cls.IO_BYTEORDER)
        data = src.read(data_size)
        return data

    @classmethod
    def _write_enckey(cls, dst: BinaryIO, data: bytes):
        dst.write(len(data).to_bytes(length=cls.ENCKEY_SIZE_LEN, byteorder=cls.IO_BYTEORDER))
        dst.write(data)

    def _get_sealer(self) -> SCellSeal:
        return self.__sealer


class PeerMsgKeypair:

    def __init__(self) -> None:
        self._keypair = GenerateKeyPair(KEY_PAIR_TYPE.EC)

    @property
    def pubkey(self) -> bytes:
        return self._keypair.export_public_key()

    @property
    def privkey(self) -> bytes:
        return self._keypair.export_private_key()


class PeerMsgSealer:
    TRUNK_SIZE = 10 * 1024 * 1024  # 10 MB
    trunk_io = TrunkIO(trunk_size=TRUNK_SIZE, len_size=8, len_byteorder='little')

    def __init__(self, self_privkey: bytes, peer_pubkey: bytes) -> None:
        self._sealer = SMessage(private_key=self_privkey, peer_public_key=peer_pubkey)

    def wrap(self, data: bytes) -> bytes:
        return self._sealer.wrap(data)

    def unwrap(self, data: bytes) -> bytes:
        return self._sealer.unwrap(data)

    def wrap_file_in_trunks(self, src_file: BinaryIO, dst_file: BinaryIO):
        """Encrypts a potentially large file in trunks.

        NOTE: The files are not closed by this method.

        Args:
          src_file: source file, should be opened in readable binary mode and positioned to the starting location
          dst_file: destination file, should be opened in writable binary mode and positioned to the starting location
        """
        self.trunk_io.proc_file_in_trunks(src_file=src_file, dst_file=dst_file,
                                          read_mode=TrunkIO.Mode.BYTES, write_mode=TrunkIO.Mode.LEN_BYTES,
                                          proc_func=self._sealer.wrap)

    def unwrap_file_in_trunks(self, src_file: BinaryIO, dst_file: BinaryIO):
        """Decrypts a potentially large file in trunks.

        NOTE: The files are not closed by this method.

        Args:
          src_file: source file, should be opened in readable binary mode and positioned to the starting location
          dst_file: destination file, should be opened in writable binary mode and positioned to the starting location
        """
        self.trunk_io.proc_file_in_trunks(src_file=src_file, dst_file=dst_file,
                                          read_mode=TrunkIO.Mode.LEN_BYTES, write_mode=TrunkIO.Mode.BYTES,
                                          proc_func=self._sealer.unwrap)
