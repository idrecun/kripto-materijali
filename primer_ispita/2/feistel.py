from typing import List, Callable
from bits import xor, bits_to_blocks, bits_from_blocks


def feistel_round(left: List[int], right: List[int], key: List[int], F: Callable[[List[int], List[int]], List[int]]):
    # TODO: Implement Feistel round
    return right, xor(left, F(right, key))


def feistel_inverse(left: List[int], right: List[int], key: List[int], F: Callable[[List[int], List[int]], List[int]]):
    # TODO: Implement inverse Feistel round
    return xor(right, F(left, key)), left


def feistel_encrypt(plaintext: List[int], keys: List[List[int]], F: Callable[[List[int], List[int]], List[int]], rounds: int) -> List[int]:
    left, right = bits_to_blocks(plaintext, len(plaintext) // 2)
    # TODO: Implement Feistel rounds loop
    for i in range(rounds):
        left, right = feistel_round(left, right, keys[i], F)
    return bits_from_blocks([left, right])


def feistel_decrypt(ciphertext: List[int], keys: List[List[int]], F: Callable[[List[int], List[int]], List[int]], rounds: int) -> List[int]:
    left, right = bits_to_blocks(ciphertext, len(ciphertext) // 2)
    # TODO: Implement inverse rounds loop
    for i in range(rounds):
        left, right = feistel_inverse(left, right, keys[rounds - i - 1], F)
    return bits_from_blocks([left, right])


def example_F(right: List[int], key: List[int]) -> List[int]:
    return xor(right, key)


