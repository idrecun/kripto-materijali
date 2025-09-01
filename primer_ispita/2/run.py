from typing import List
from bits import bits_to_bitstring
from feistel import feistel_encrypt, feistel_decrypt, example_F
from modes import ecb_encrypt, ecb_decrypt


if __name__ == "__main__":
    block_size = 16
    rounds = 4
    # Round keys (one per round), same size as half-block (8 bits)
    keys: List[List[int]] = [
        [0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
    ]

    # Two-block plaintext for ECB (32 bits total)
    plaintext: List[int] = [
        0, 0, 0, 1, 0, 0, 1, 0,  0, 1, 0, 0, 1, 1, 0, 0,
        1, 1, 0, 0, 0, 1, 1, 0,  1, 0, 1, 1, 0, 0, 0, 1,
    ]

    enc_block = lambda block, _k: feistel_encrypt(block, keys, example_F, rounds)
    dec_block = lambda block, _k: feistel_decrypt(block, keys, example_F, rounds)

    c = ecb_encrypt(enc_block, plaintext, block_size, keys[0])
    m = ecb_decrypt(dec_block, c, block_size, keys[0])
    print(f"ECB decrypt OK: {m == plaintext}")
    print(f"Ciphertext: {bits_to_bitstring(c)}")


