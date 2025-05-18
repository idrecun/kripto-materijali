# Impelment an SP network
import random
from bits import bits_to_blocks, bits_from_blocks, bits_to_int, bits_from_int, xor


def generate_random_key(block_size):
    return [random.randint(0, 1) for _ in range(block_size)]


def substitute(state, sbox):
    nibbles = bits_to_blocks(state, 4)
    substituted = [bits_from_int(sbox[bits_to_int(nibble)], 4) for nibble in nibbles]
    return bits_from_blocks(substituted)


def permute(state, pbox):
    return [state[p] for p in pbox]


def sp_encrypt(plaintext, keys, sbox, pbox, rounds):
    state = plaintext[:]
    for i in range(rounds):
        state = xor(state, keys[i])
        state = substitute(state, sbox)
        state = permute(state, pbox)
    state = xor(state, keys[-1])
    return state


def sp_decrypt(ciphertext, keys, sbox, pbox, rounds):
    state = ciphertext[:]
    state = xor(state, keys[-1])
    for i in range(rounds - 1, -1, -1):
        state = permute(state, pbox)
        state = substitute(state, sbox)
        state = xor(state, keys[i])
    return state


# Example usage
if __name__ == "__main__":
    block_size = 16
    sbox = [
        0x6,
        0x4,
        0xC,
        0x5,
        0x0,
        0x7,
        0x2,
        0xE,
        0x1,
        0xF,
        0x3,
        0xD,
        0x8,
        0xA,
        0x9,
        0xB,
    ]
    pbox = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
    rounds = 4

    # Calculate inverse boxes
    inverse_sbox = {v: k for k, v in enumerate(sbox)}
    inverse_pbox = [0] * len(pbox)
    for i, p in enumerate(pbox):
        inverse_pbox[p] = i

    # Generate random keys
    keys = [generate_random_key(block_size) for _ in range(rounds + 1)]

    # Example plaintext (16-bit block)
    plaintext = [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0]

    # Encrypt and decrypt
    ciphertext = sp_encrypt(plaintext, keys, sbox, pbox, rounds)
    decrypted = sp_decrypt(ciphertext, keys, inverse_sbox, inverse_pbox, rounds)

    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted:  {decrypted}")
