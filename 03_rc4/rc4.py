from getpass import getpass

# Key scheduling algorithm
def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256   # j += S[i] + K[i]
        S[i], S[j] = S[j], S[i]                      # swap(S[i], K[i])
    return S

# Pseudo-random generation algorithm
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256            # i += 1
        j = (j + S[i]) % 256         # j += S[i]
        S[i], S[j] = S[j], S[i]      # swap(S[i], S[j])
        K = S[(S[i] + S[j]) % 256]   # K = S[S[i] + S[j]]
        yield K

# Encryption / decryption of 'data' using 'key'
def RC4(key, data):
    key = [ord(c) for c in key]
    S = KSA(key)
    keystream = PRGA(S)
    transformed = bytes(byte ^ next(keystream) for byte in data)
    return transformed

def encrypt(key, plaintext):
    encoded = plaintext.encode('ascii')
    encrypted = RC4(key, encoded)
    return encrypted.hex()

def decrypt(key, ciphertext):
    encoded = bytes.fromhex(ciphertext)
    decrypted = RC4(key, encoded)
    return decrypted.decode('ascii')

# Example usage:
plaintext = input('Enter message:')
key = getpass('Enter key:')
encrypted_text = encrypt(key, plaintext)
decrypted_text = decrypt(key, encrypted_text)

print('Plaintext:', plaintext)
print('Encrypted:', encrypted_text)
print('Decrypted:', decrypted_text)

