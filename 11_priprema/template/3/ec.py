class Curve:
    def __init__(self, a, b, p, n=0):
        self.a = a
        self.b = b
        self.p = p
        self.n = n
        self.encoding_factor = 32

    def encode_message(self, m):
        # Implement me

    def decode_message(self, M):
        # Implement me

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
        if self.x == other.x and self.y != other.y:
            return Point(self.curve, None, None)  
        if self == -other:
            return Point(self.curve, None, None)  

        # Implement me

        return Point(self.curve, x3, y3)

    def __rmul__(self, scalar):
        result = Point(self.curve, None, None)  
        point  = Point(self.curve, self.x, self.y)  

        
        while scalar > 0:
            if scalar % 2 == 1:
                result = result + point  
            scalar //= 2  
            point = point + point  

        return result

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
secp256k1 = Curve(a, b, p, n)
Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
G = Point(secp256k1, Gx, Gy)
