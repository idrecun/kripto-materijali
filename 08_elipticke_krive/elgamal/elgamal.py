import ec
import diffie_hellman as dh

def encode(message):
    return ec.secp256k1.encode_message(int(message.encode('utf-8').hex(), 16))

def decode(message):
    return bytes.fromhex(hex(ec.secp256k1.decode_message(message))[2:]).decode('utf-8')

def encrypt(priv_key, oth_pub_key, message):
    S = dh.shared_key(priv_key, oth_pub_key)
    return S + message

def decrypt(priv_key, oth_pub_key, ciphertext):
    S = dh.shared_key(priv_key, oth_pub_key)
    return -S + ciphertext
