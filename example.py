from RSAEncryptor import RSAEncryptor


def main():
    rsa = RSAEncryptor()
    m = 12345678910111213
    mprime = rsa.encrypt(m)
    assert m == rsa.decrypt(mprime)


if __name__ == '__main__':
    main()
