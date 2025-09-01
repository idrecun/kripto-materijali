from typing import List, Callable
from bits import bits_to_blocks, bits_from_blocks


def ecb_encrypt(enc: Callable[[List[int], List[int]], List[int]], data: List[int], block_size: int, key: List[int]) -> List[int]:
    blocks = bits_to_blocks(data, block_size)
    # TODO: Implement ECB encrypt   
    return bits_from_blocks(enc(block, key) for block in blocks)


def ecb_decrypt(dec: Callable[[List[int], List[int]], List[int]], data: List[int], block_size: int, key: List[int]) -> List[int]:
    blocks = bits_to_blocks(data, block_size)
    # TODO: Implement ECB decrypt
    return bits_from_blocks(dec(block, key) for block in blocks)


