from typing import List, Tuple, Iterator


def lfsr_step(state: List[int], taps: List[int]) -> Tuple[List[int], int]:
    # TODO: Implement LFSR step
    feedback = 0
    for tap in taps:
        feedback ^= state[tap - 1]
    output = state[-1]
    state = [feedback] + state[:-1]
    return state, output


def lfsr_run(seed: List[int], taps: List[int]) -> Iterator[int]:
    # TODO: Implement LFSR generator
    state = seed[:]
    while True:
        state, bit = lfsr_step(state, taps)
        yield int(bit)


