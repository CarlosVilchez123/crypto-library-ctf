from Crypto.Util.number import long_to_bytes as l2b
from Crypto.Util.number import bytes_to_long as b2l
import gmp2 

def encrypt_rsa(message, public_key):
    m = b2l(message)

    e, n = public_key

    message_encrypt = gmp2.iroot(m, e, n)

    return c

def decrypt_rsa(message_encryp, private_key):
    m = b2l(message_encryp)

    d, n = private_key

    message_decrypt = gmp2.iroot(m, d, n)

    return l2b(message_decrypt)