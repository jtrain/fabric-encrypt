from fabric_encrypt.backends.gpg import GPG

_DEFAULT_BACKEND = GPG()

def set_default_backend(backend):
    global _DEFAULT_BACKEND
    _DEFAULT_BACKEND = backend

def get_default_backend():
    return _DEFAULT_BACKEND
