def mono_str(n):
    if n == 0:
        return '1'
    if n == 1:
        return 'x'
    return 'x^' + str(n)

def poly_str(p):
    monomials = []
    power = 0
    while p:
        if p & 1:
            monomials.append(power)
        p >>= 1
        power += 1
    monomials.reverse()
    return ' + '.join(mono_str(m) for m in monomials)


def poly_mul(p1, p2):
    product = 0
    while p1:
        if p1 & 1:
            product ^= p2
        p1 >>= 1
        p2 <<= 1
    return product

def poly_mul_mod(p1, p2, mod):
    product = 0
    while p1:
        if p1 & 1:
            product ^= p2
        p1 >>= 1
        p2 <<= 1
        if p2 & (1 << (mod.bit_length() - 1)):
            p2 ^= mod
    return product

def poly_div(p1, p2):
    quotient = 0
    while p1.bit_length() >= p2.bit_length():
        diff = p1.bit_length() - p2.bit_length()
        quotient |= 1 << diff
        p1 ^= p2 << diff
    return quotient

def poly_mod(p, mod):
    while p.bit_length() >= mod.bit_length():
        diff = p.bit_length() - mod.bit_length()
        p ^= mod << diff
    return p

def poly_gcd(p1, p2):
    x1, x2 = 1, 0
    y1, y2 = 0, 1

    while p2 != 0:
        q = poly_div(p1, p2)
        p1, p2 = p2, p1 ^ poly_mul(q, p2)
        x1, x2 = x2, x1 ^ poly_mul(q, x2)
        y1, y2 = y2, y1 ^ poly_mul(q, y2)

    return (p1, x1, y1)

def poly_inv(p, mod):
    (_, p_inv, _) = poly_gcd(p, mod)
    return poly_mod(p_inv, mod)
