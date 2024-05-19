from django.test import TestCase
from api.utils.cipher import HSACipher
from backend.settings import CIPHER_KEY


class TestHSACipher(TestCase):
    def test_encrypt_and_decrypt(self):
        # Test encryption and decryption
        plaintext = "Hello, World!"
        ciphertext = HSACipher.encrypt(plaintext)
        decrypted_text = HSACipher.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted_text)

    def test_encrypt_with_custom_key(self):
        # Test encryption with a custom key
        plaintext = "Secret message"
        key = "Vee/q6I9RTQMANpL/M1Or7eMix5HxlQG"
        if len(key) in [16, 24, 32]:
            ciphertext = HSACipher.encrypt(plaintext, key)
            decrypted_text = HSACipher.decrypt(ciphertext, key)
            self.assertEqual(plaintext, decrypted_text)
        else:
            self.assertRaises(ValueError, HSACipher.encrypt, plaintext, key)
