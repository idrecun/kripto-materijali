from math import isqrt
# n = p * q = (s - t) (s + t)
# n = s^2 - t^2
# t^2 = s^2 - n
# t = isqrt(s^2 - n)
def factorize(n):
    s = isqrt(n)
    if s * s == n:
        return s, s
    s += 1
    while s < n:
        t2 = s ** 2 - n
        t = isqrt(t2)
        if t * t == t2:
            return s - t, s + t
        s += 1

print(factorize(int(input())))
