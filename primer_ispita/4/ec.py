class Curve:
    def __init__(self, a, b, p, n=0):
        self.a = a
        self.b = b
        self.p = p
        self.n = n


class Point:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x % curve.p if x is not None else None
        self.y = y % curve.p if y is not None else None

    def is_infinite(self):
        return self.x is None and self.y is None

    def __neg__(self):
        if self.is_infinite():
            return self
        return Point(self.curve, self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if self.is_infinite():
            return other
        if other.is_infinite():
            return self
        if self == -other:
            return Point(self.curve, None, None)

        # TODO: Implement the two primary slope formulas (addition vs doubling)
        if self != other:
            s = ((other.y - self.y) * pow((other.x - self.x) % self.curve.p, -1, self.curve.p)) % self.curve.p
        else:
            s = ((3 * (self.x ** 2) + self.curve.a) * pow((2 * self.y) % self.curve.p, -1, self.curve.p)) % self.curve.p

        # TODO: Compute resulting coordinates using x3 = s^2 - x1 - x2 and y3 = s(x1 - x3) - y1
        x = (s * s - self.x - other.x) % self.curve.p
        y = (s * (self.x - x) - self.y) % self.curve.p
        return Point(self.curve, x, y)

    def __rmul__(self, k):
        result = Point(self.curve, None, None)
        addend = self
        while k > 0:
            if k & 1:
                result = result + addend
            k >>= 1
            addend = addend + addend
        return result


p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0
b = 7
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
secp256k1 = Curve(a, b, p, n)
Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
G = Point(secp256k1, Gx, Gy)


