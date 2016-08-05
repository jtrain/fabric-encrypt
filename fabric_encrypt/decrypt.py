from contextlib import contextmanager

from fabric.api import local

from .backends import gpg

DEFAULT_BACKEND = gpg.GPG()

@contextmanager
def decrypt(encrypted_filename, backend=None):

    if not backend:
        backend = DEFAULT_BACKEND

    cmd_string = backend.decrypt(encrypted_filename)
    return local(cmd_string)
