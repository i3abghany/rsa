from unittest import TestCase

import Encode
from RSAEncryptor import RSAEncryptor


class TestRSAEncryptor(TestCase):

    def test_encrypt_small_message(self):
        m = 'Seat thyself sultanically among the moons of Saturn'
        rsa = RSAEncryptor()
        enc = rsa.encrypt(Encode.to_numeric(m))
        dec = Encode.to_string(rsa.decrypt(enc))
        self.assertEqual(m, dec)

    def test_numeric_message(self):
        m = 656112132172731831939213281327132
        rsa = RSAEncryptor()
        enc = rsa.encrypt(m)
        dec = rsa.decrypt(enc)
        self.assertEqual(m, dec)

    def test_encrypt_message_larger_than_mod(self):
        rsa = RSAEncryptor()
        mod = rsa._mod
        m = mod + 1
        self.assertRaises(RuntimeError, lambda: rsa.encrypt(m))
