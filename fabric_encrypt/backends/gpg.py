import os

from .base import EncryptBase


class GPG(EncryptBase):

    programs = ['gpg2', 'gpg']
    decrypt_arguments = '-d'

    def prime_cache(self):
        program = self._get_program()
        local("echo '' | {program} -s".format(program=program))
