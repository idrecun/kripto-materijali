from lfsr import lfsr_run


if __name__ == "__main__":
    seed = [1, 0, 0, 1]
    taps = [1, 4]
    gen = lfsr_run(seed, taps)
    print("".join(str(next(gen)) for _ in range(64)))


