import contextlib
import os
import tempfile

from fabric.api import local, settings


class EncryptBase(object):

    command_template = "{program} {arguments} {encrypted_filename}"

    class ProgramNotFound(Exception):
        pass

    def on_decrypt(self):
        """
        Hook to run any command before decrypting.
        """

    @contextlib.contextmanager
    def decrypt_string(self, encrypted_filename):

        self.on_decrypt()
        program = self._get_program()
        arguments = self._get_decrypt_arguments(encrypted_filename)
        command = self._build_command(program, arguments, encrypted_filename)
        yield local(command, capture=True)

    @contextlib.contextmanager
    def decrypt(self, encrypted_filename):

        self.on_decrypt()
        with self.decrypt_string(encrypted_filename) as contents:
            try:
                fd, plaintext_filename = self._get_destination(encrypted_filename)
                with open(plaintext_filename, "wb") as fo:
                    fo.write(contents)
                yield plaintext_filename
            finally:
                os.close(fd)
                os.remove(plaintext_filename)

    def prime_cache(self):
        """
        Do some trivial work in order to force the password to be
        entered and hence prime the cache.
        """

    def _build_command(self, program, arguments, encrypted_filename):
        """
        Builds a command that will decrypt and return a string
        of the contents.
        """

        return self.command_template.format(
            program=program, arguments=arguments, encrypted_filename=encrypted_filename
        )

    def _get_decrypt_arguments(self, encrypted_filename):
        return self.decrypt_arguments

    def _get_destination(self, encrypted_filename):
        return tempfile.mkstemp()

    def _get_program(self):
        for name in self.programs:
            try:
                return self._which_program(name)
            except self.ProgramNotFound:
                pass

        raise self.ProgramNotFound(
            u"Unable to local any of {}".format(", ".join(self.programs))
        )

    def _which_program(self, name):
        with settings(abort_exception=self.ProgramNotFound):
            program = local("which " + name, capture=True)
            if not program:
                raise self.ProgramNotFound
            return program
