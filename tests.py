from ctf_crypto_lib import cipher_XOR, decode_XOR

print(cipher_XOR("hola", "key"))
print(decode_XOR("00000011000010100001010100001010", "key"))