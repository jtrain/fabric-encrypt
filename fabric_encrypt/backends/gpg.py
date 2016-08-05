import os

from .base import EncryptBase


class GPG(EncryptBase):

    programs = ['gpg2', 'gpg']
    decrypt_arguments = '-d'
