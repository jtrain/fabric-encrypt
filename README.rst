Fabric-encrypt is a Python 2.7 library for encrypting and decrypting secrets,
it was designed to be used with Fabric.

Storing secrets like your API secret keys, deployment ssh keys, django secrets
and other things in plaintext alongside your deploy scripts isn't recommended.
Instead, encrypt those secrets and check them into your source code. We can go
one better, and allow access management to those secrets so some members of
your team can have production access, while others can have preproduction.

A typical usage of the tool may look like this.

.. code-block:: python
    import StringIO

    from fabric import api
    from fabric_encrypt import decrypt


    def deploy():
        # decrypt ascii armoured gpg file, destroyed once finished.
        with decrypt('secrets/django_secrets.py.asc') as local_filename:
            api.put(remote_path='/www/deploy/conf/secrets.py',
                    local_path=local_filename)

        # decrypt ascii armoured gpg file into string.
        with decrypt_string('secrets/django_secrets.py.asc') as secrets:
            api.put(local_path=StringIO.StringIO(secrets),
                    remote_path='/www/deploy/conf/secrets.py')
```

If using ``gpg-agent`` or ``gpg2`` you will only be prompted for the password
once.

