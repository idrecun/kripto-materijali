import block_cipher as bc

def encrypt(b, K):
    if len(b) % 2 == 1:
        b = b + '\0'

    c = []
    for i in range(0, len(b), 2):
        c.append(bc.encryptBlock([b[i], b[i+1]], K))
    c = sum(c, [])

    return bytearray(c)

def decrypt(b, K):
    m = []
    for i in range(0, len(b), 2):
        m.append(bc.decryptBlock([b[i], b[i+1]], K))
    m = sum(m, [])

    return bytes(m)

if __name__ == '__main__':
    message = "Hello!"
    key = "xD"

    messageBytes = message.encode('utf-8')
    messageHex = messageBytes.hex()
    print(f'Poruka (hex): {messageHex}')

    K = key.encode('utf-8')

    ciphertextBytes = encrypt(messageBytes, K)
    ciphertextHex = ciphertextBytes.hex()
    print(f'Šifrat (hex): {ciphertextHex}')

    decryptedBytes = decrypt(ciphertextBytes, K)
    decrypted = decryptedBytes.decode('utf-8')
    print(f'Dešifrovano:  {decrypted}')
