import os
import sys
from getpass import getpass

def xor_bytes(bytes1, bytes2):
    return bytes(x ^ y for x, y in zip(bytes1, bytes2))


# Read the plaintext message from standard input
message = input('Enter message: ')

# Convert the message to bytes
message_bytes = message.encode('ascii')

# Read the encryption key from standard input
key = getpass('Enter key: ')

# Convert the key to bytes
key_bytes = key.encode('ascii')

# Adjust key length to match message length
repeats = len(message_bytes) // len(key_bytes) + 1
key_bytes = (repeats * key_bytes)[:len(message_bytes)]

# XOR the message with the key
ciphertext_bytes = xor_bytes(message_bytes, key_bytes)

# Convert the byte strings to hexadecimal representation
hex_message = message_bytes.hex()
hex_ciphertext = ciphertext_bytes.hex()

# Output the results
print(f'Message hex:    {hex_message}')
print(f'Ciphertext hex: {hex_ciphertext}')
