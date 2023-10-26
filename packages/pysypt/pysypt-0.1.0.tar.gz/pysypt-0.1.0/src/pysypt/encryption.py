import os
import subprocess
from pathlib import Path

src_dir = Path(__file__).parent / "../"
executable_name = "encryption-app.bat" if os.name == 'nt' else "encryption-app"

EXECUTABLE_PATH = src_dir / "java/encryption-app/build/distributions/encryption-app-1.0-SNAPSHOT/bin" / executable_name


def _run_command(command: str) -> str:
    """Calls `command` in shell and returns its output as string.

    :param command: the command to perform.
    :return: terminal output of the command.
    """
    p = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        shell=True)
    encrypted, _ = p.communicate()
    p.wait()
    return encrypted.decode('utf-8')


def decrypt(message: str, key: str) -> str:
    """Uses external java app for decrypting message with jasypt.

    :param message: the message to decrypt.
    :param key: the key used for decrypting the message.
    :return: the plaintext message.
    """
    return _run_command(
        f'{EXECUTABLE_PATH} --decrypt --key "{key}" --message "{message}"'
    )


def encrypt(message: str, key: str):
    """Uses external java app for encrypting message with jasypt.

        :param message: the message to encrypt.
        :param key: the key used for encrypting the message.
        :return: the plaintext message.
        """
    return _run_command(
        f'{EXECUTABLE_PATH} --encrypt --key "{key}" --message "{message}"'
    )
