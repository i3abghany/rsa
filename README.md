# rsa

A simple implementation of the RSA asymmetric cipher. It only supports encrypting messages encoded as integers less
than the internally-generated RSA mod. This is because, typically, RSA is only used to exchange symmetric cipher keys,
which are usually much smaller than RSA keys.