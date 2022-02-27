from unittest import TestCase

import Encode


class TestEncode(TestCase):
    def test_to_numeric(self):
        m = 'hello from encode test!'
        res = 0
        base = 1
        for c in m:
            res += (ord(c) * base)
            base *= 256
        self.assertEqual(res, Encode.to_numeric(m))

    def test_to_string(self):
        m = 19823712893712918273192837189
        decoded = Encode.to_string(m)
        res = str()
        while m > 0:
            res += chr(m % 256)
            m = m // 256
        self.assertEqual(res, decoded)
