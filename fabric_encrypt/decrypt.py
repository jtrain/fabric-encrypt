from contextlib import contextmanager

from fabric_encrypt.backends import get_default_backend

@contextmanager
def decrypt(encrypted_filename, backend=None):

    if not backend:
        backend = get_default_backend()

    with backend.decrypt(encrypted_filename) as filename:
        yield filename

@contextmanager
def decrypt_string(encrypted_filename, backend=None):

    if not backend:
        backend = get_default_backend()

    with backend.decrypt_string(encrypted_filename) as content:
        yield content

