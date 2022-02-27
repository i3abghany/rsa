import Encode
from RSAEncryptor import RSAEncryptor


def main():
    rsa = RSAEncryptor()
    m = 'hello world'
    mprime = rsa.encrypt(Encode.to_numeric(m))
    assert m == Encode.to_string(rsa.decrypt(mprime))


if __name__ == '__main__':
    main()
