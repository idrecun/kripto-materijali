import os
import sys
from getpass import getpass
from poly import *

def word_to_nibbles(byte):
    return ((byte >> 4) & 0x0F, byte & 0x0F)

def nibbles_to_word(N0, N1):
    return (N0 << 4) | N1 

# Forward functions

def S1(N):
    return poly_inv(N, 0b10011)

def S2(N):
    return poly_mul_mod(0b1101, N, 0b10001) ^ 0b1001

def SN(N):
    return S2(S1(N))

def SW(W):
    N0, N1 = word_to_nibbles(W)
    return nibbles_to_word(SN(N0), SN(N1))

def R(W):
    N0, N1 = word_to_nibbles(W)
    return nibbles_to_word(N1, N0)

def KSA(K0):
    W0, W1 = K0[0], K0[1]

    C1 = nibbles_to_word(poly_mod((1 << (1 + 2)), 0b10001), 0)
    W2 = W0 ^ C1 ^ SW(R(W1))
    W3 = W1 ^ W2

    K1 = bytes([W2, W3])

    C2 = nibbles_to_word(poly_mod((1 << (2 + 2)), 0b10001), 0)
    W4 = W2 ^ C2 ^ SW(R(W3))
    W5 = W3 ^ W4

    K2 = bytes([W4, W5])

    return [K0, K1, K2]

def D(K, B):
    return [K[0] ^ B[0], K[1] ^ B[1]]

def S(B):
    return [SW(B[0]), SW(B[1])]

def Z(B):
    N0, N1 = word_to_nibbles(B[0])
    N2, N3 = word_to_nibbles(B[1])

    return [nibbles_to_word(N0, N3), nibbles_to_word(N2, N1)]

def M(B):
    # (ai + b) * (ci + d) = (ad + bc)i + (bd - ac)
    # zamenimo ci+d = x^2i + 1
    # (a + bx^2)i + (b + ax^2)
    N0, N1 = word_to_nibbles(B[0])
    T0 = N0 ^ poly_mul_mod(N1, 0b100, 0b10011)
    T1 = N1 ^ poly_mul_mod(N0, 0b100, 0b10011)

    N2, N3 = word_to_nibbles(B[1])
    T2 = N2 ^ poly_mul_mod(N3, 0b100, 0b10011)
    T3 = N3 ^ poly_mul_mod(N2, 0b100, 0b10011)

    return [nibbles_to_word(T0, T1), nibbles_to_word(T2, T3)]

def SAES(B, K0, K1, K2):
    return D(K2, Z( S( D(K1, M( Z( S( D(K0, B) ) ) ) ) ) ) )

# Inverse functions

def Dinv(K, B):
    return D(K, B)

def S1inv(N):
    return S1(N)

def S2inv(N):
    return poly_mul_mod(0b111, N, 0b10001) ^ 0b1100

def SNinv(N):
    return S1inv(S2inv(N))

def SWinv(W):
    N0, N1 = word_to_nibbles(W)
    return nibbles_to_word(SNinv(N0), SNinv(N1))

def Sinv(B):
    return [SWinv(B[0]), SWinv(B[1])]

def Zinv(B):
    return Z(B)

def Minv(B):
    # (x)i + (x^3 + 1)
    N0, N1 = word_to_nibbles(B[0])
    T0 = poly_mul_mod(N1, 0b10, 0b10011) ^ poly_mul_mod(N0, 0b1001, 0b10011)
    T1 = poly_mul_mod(N0, 0b10, 0b10011) ^ poly_mul_mod(N1, 0b1001, 0b10011)

    N2, N3 = word_to_nibbles(B[1])
    T2 = poly_mul_mod(N3, 0b10, 0b10011) ^ poly_mul_mod(N2, 0b1001, 0b10011)
    T3 = poly_mul_mod(N2, 0b10, 0b10011) ^ poly_mul_mod(N3, 0b1001, 0b10011)

    return [nibbles_to_word(T0, T1), nibbles_to_word(T2, T3)]

def SAESinv(B, K0, K1, K2):
    return Dinv(K0, Zinv( Sinv( Minv( Dinv(K1, Zinv( Sinv( Dinv(K2, B) ) ) ) ) ) ) )


# Read the plaintext message from standard input
message = input('Enter message: ')

# Pad the message to an even number of bytes
if len(message) % 2 != 0:
    message = message + message[0]

# Convert the message to bytes
message_bytes = message.encode('ascii')

# Extract two-byte blocks
num_blocks = len(message_bytes) // 2
blocks = [ message_bytes[2 * i : 2 * (i + 1)] for i in range(num_blocks) ]

# Read the encryption key from standard input
key = getpass('Enter key: ')

# Key length must be 2
if len(key) != 2:
    print('Key length must be 2 bytes')
    quit()

# Convert the key to bytes
key_bytes = key.encode('ascii')

# Expand key
K0, K1, K2 = KSA(key_bytes)

# Encrypt all blocks
ciphertext_blocks = [ SAES(B, K0, K1, K2) for B in blocks ]
ciphertext_bytes = bytes( byte for block in ciphertext_blocks for byte in block )

# Decrypt all blocks
deciphered_blocks = [ SAESinv(B, K0, K1, K2) for B in ciphertext_blocks ]
deciphered_bytes = bytes( byte for block in deciphered_blocks for byte in block )

# Convert the byte strings to hexadecimal representation
hex_message = message_bytes.hex()
hex_ciphertext = ciphertext_bytes.hex()
hex_deciphered = deciphered_bytes.hex()

# Output the results
print(f'Message hex:    {hex_message}')
print(f'Ciphertext hex: {hex_ciphertext}')
print(f'Deciphered hex: {hex_deciphered}')
