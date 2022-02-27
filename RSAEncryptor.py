
try:
    from Cryptodome.Util import number
except ModuleNotFoundError:
    import pip

    pip.main(['install', 'pycryptodomex'])
finally:
    from Cryptodome.Util import number


class RSAEncryptor:
    DEFAULT_PUBLIC_EXPONENT = 65537

    def __init__(self, prime_length=1024):
        self.prime_length = prime_length
        self._gen_keys()

    def _gen_keys(self):
        self._p = number.getPrime(self.prime_length)
        self._q = number.getPrime(self.prime_length)
        self._mod = (self._p - 1) * (self._q - 1)
        self._n = self._p * self._q
        self._e = self.DEFAULT_PUBLIC_EXPONENT
        self._d = pow(self._e, -1, self._mod)

    def encrypt(self, m: int):
        # In RSA, the encoded message must be less than the calculated product of `p` and `q`.
        # The way we encode messages is problematic since the numeric message can increase
        # very quickly. We could divide the message into multiple parts, encode and encrypt
        # them transparently from the user. However, RSA is usually only used to securely
        # exchange keys for another symmetric cypher such as AES, and use it from there.
        # Since AES keys are usually 256 bits at most, we won't suffer from larger-than-mod
        # message issues.
        if m >= self._n:
            raise RuntimeError('Encoded message larger than internally-generated mod.')
        return pow(m, self._e, self._n)

    def decrypt(self, m_prime: int):
        return pow(m_prime, self._d, self._n)
