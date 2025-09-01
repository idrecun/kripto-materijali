from diffie_hellman import private_key, public_key, shared_key


if __name__ == "__main__":
    a = private_key()
    b = private_key()
    A = public_key(a)
    B = public_key(b)

    s1 = shared_key(a, B)
    s2 = shared_key(b, A)
    print(f"Shared key OK: {s1 == s2}")


