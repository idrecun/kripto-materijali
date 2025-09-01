from typing import List


def bits_to_bitstring(b: List[int]) -> str:
    return "".join(map(str, b))


def bits_to_blocks(b: List[int], size: int) -> List[List[int]]:
    padded = b[:]
    pad_bits = (-len(b)) % size
    padded.extend([0] * pad_bits)
    return [padded[i : i + size] for i in range(0, len(padded), size)]


def bits_from_blocks(s: List[List[int]]) -> List[int]:
    return [int(bit) for block in s for bit in block]


def xor(a: List[int], b: List[int]) -> List[int]:
    return [x ^ y for x, y in zip(a, b)]


