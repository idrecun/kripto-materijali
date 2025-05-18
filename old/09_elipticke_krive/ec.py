class Curve:
    def __init__(self, a, b, p, n=0):
        self.a = a
        self.b = b
        self.p = p
        self.n = n
        self.encoding_factor = 32

    def is_non_singular(self):
        return (4 * pow(self.a, 3, self.p) + 27 * pow(self.b, 2, self.p)) % self.p != 0

    def encode_message(self, m):
        for i in range(self.encoding_factor):
            x = m * self.encoding_factor + i
            y2 = (x ** 3 + self.a * x + self.b) % self.p
            if pow(y2, (self.p - 1) // 2, self.p) == 1:  # Euler's criterion
                y = pow(y2, (self.p + 1) // 4, self.p)   # Modular square root when p = 3 (mod 4)
                return Point(self, x, y)

    def decode_message(self, M):
        return M.x // self.encoding_factor

class Point:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y
        if self.x is not None:
            self.x %= curve.p
        if self.y is not None:
            self.y %= curve.p

    def is_infinite(self):
        return self.x is None and self.y is None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        if self.is_infinite():
            return self
        return Point(self.curve, self.x, -self.y)

    def __add__(self, other):
        if self.is_infinite():
            return other
        if other.is_infinite():
            return self
        if self == -other:
            return Point(self.curve, None, None)  # Identity point

        if self != other:
            s = ((other.y - self.y) * pow(other.x - self.x, -1, self.curve.p)) % self.curve.p
        else:
            s = ((3 * self.x ** 2 + self.curve.a) * pow(2 * self.y, -1, self.curve.p)) % self.curve.p

        x = (s ** 2 - self.x - other.x) % self.curve.p
        y = (s * (self.x - x) - self.y) % self.curve.p

        return Point(self.curve, x, y)

    def __rmul__(self, scalar):
        result = Point(self.curve, None, None)  # Initialize with the identity point
        point  = Point(self.curve, self.x, self.y)  # Initialize with self

        # Perform double-and-add algorithm
        while scalar > 0:
            if scalar % 2 == 1:
                result = result + point  # Add the point if the bit is 1
            scalar //= 2  # Halve the scalar
            point = point + point  # Double the point

        return result

    def __str__(self):
        if self.is_infinite():
            return "Infinity"
        else:
            return f"({hex(self.x)}, {hex(self.y)})"

# EC 256-bit parameters
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
secp256k1 = Curve(a, b, p, n)
Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
G = Point(secp256k1, Gx, Gy)
