# Implements the shrinking generator
from lfsr import lfsr_run


def shrinking_generator(seed1, taps1, seed2, taps2):
    lfsr1_gen = lfsr_run(seed1, taps1)
    lfsr2_gen = lfsr_run(seed2, taps2)

    while True:
        control_bit = next(lfsr1_gen)
        output_bit = next(lfsr2_gen)

        if control_bit == 1:
            yield output_bit


# Example usage
if __name__ == "__main__":
    seed1 = [1, 0, 1, 1]
    taps1 = [1, 3]
    seed2 = [1, 1, 0, 1]
    taps2 = [2, 4]

    sg = shrinking_generator(seed1, taps1, seed2, taps2)

    output = [next(sg) for _ in range(20)]  # Generate 20 bits
    print("Output bits:", output)
