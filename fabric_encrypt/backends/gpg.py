import os

from fabric.api import local

from fabric_encrypt.backends.base import EncryptBase


class GPG(EncryptBase):

    programs = ["gpg2", "gpg"]
    decrypt_arguments = "-d"

    def prime_cache(self):
        program = self._get_program()
        local(f"echo '' | {program} -as")
