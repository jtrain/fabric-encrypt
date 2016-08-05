from fabric.api import local

from .base import EncryptBase

class GPG(EncryptBase):

    def get_program(self):
        gpg_cmd = local('which gpg2')
        if not gpg_cmd:
            gpg_cmd = local('which gpg')
            if not gpg_cmd:
                raise RuntimeError("Could not locate gpg.")

