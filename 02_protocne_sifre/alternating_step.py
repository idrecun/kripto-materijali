# Implements the alternating-step generator based on LFSR
from lfsr import lfsr_run


def alternating_step_generator(seed1, taps1, seed2, taps2, seed3, taps3):
    lfsr1_gen = lfsr_run(seed1, taps1)
    lfsr2_gen = lfsr_run(seed2, taps2)
    lfsr3_gen = lfsr_run(seed3, taps3)

    lfsr2_state = seed2[:]
    lfsr3_state = seed3[:]

    while True:
        control_bit = next(lfsr1_gen)

        if control_bit == 0:
            bit2 = next(lfsr2_gen)
            bit3 = lfsr3_state[0]
        else:
            bit3 = next(lfsr3_gen)
            bit2 = lfsr2_state[0]

        yield bit2 ^ bit3


# Example usage
if __name__ == "__main__":
    seed1 = [1, 0, 1]
    taps1 = [1, 3]
    seed2 = [1, 1, 0, 1]
    taps2 = [2, 4]
    seed3 = [0, 1, 1, 0, 1]
    taps3 = [1, 2, 5]

    asg = alternating_step_generator(seed1, taps1, seed2, taps2, seed3, taps3)

    output = [next(asg) for _ in range(20)]
    print("Output bits:", output)
