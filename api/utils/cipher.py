# Using SECRET_KEY to encrypt and decrypt data
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from backend.settings import CIPHER_KEY


class HSACipher:
    @staticmethod
    def encrypt(plaintext: str, key: str = CIPHER_KEY):
        backend = default_backend()
        cipher = Cipher(
            algorithms.AES(key.encode("utf-8")), modes.ECB(), backend=backend
        )
        padder = padding.PKCS7(128).padder()
        padderData = padder.update(plaintext.encode("utf-8")) + padder.finalize()
        encryptor = cipher.encryptor()
        ct_bytes = encryptor.update(padderData) + encryptor.finalize()
        ct = ct_bytes.hex()
        return ct

    @staticmethod
    def decrypt(ciphertext: str, key: str = CIPHER_KEY):
        backend = default_backend()
        cipher = Cipher(
            algorithms.AES(key.encode("utf-8")), modes.ECB(), backend=backend
        )
        decryptor = cipher.decryptor()
        pt_bytes = decryptor.update(bytes.fromhex(ciphertext)) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        pt = unpadder.update(pt_bytes) + unpadder.finalize()
        pt = pt.decode("utf-8")
        return pt
