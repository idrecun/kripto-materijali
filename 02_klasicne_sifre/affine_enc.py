import os
import sys
from string import ascii_lowercase
from getpass import getpass
from math import gcd

def enc(m, k0, k1):
    if not m.islower():
        return m
    ord_m = ascii_lowercase.index(m)
    return ascii_lowercase[(k0 * ord_m + k1) % 26]

message = ""
file_path = ""
if len(sys.argv) == 2:
    file_path = sys.argv[1]
    # If an argument is provided, encrypt the file
    with open(file_path, 'r') as file:
        message = file.read()
else:
    # Read the plaintext message from standard input
    message = input('Enter message: ')


# Read the encryption key from standard input
key = getpass('Enter key: ')

# Convert characters to numbers mod 26
k0 = ascii_lowercase.index(key[0])
k1 = ascii_lowercase.index(key[1])

# Check whether key[0] and 26 are coprime
if gcd(k0, 26) != 1:
    print('Invalid key')

# Encrypt
ciphertext = "".join(enc(m, k0, k1) for m in message)

# Output the results
if file_path == "":
    print(f'Ciphertext: {ciphertext}')
else:
    with open('caesar.txt', 'w') as file:
        file.write(ciphertext)
