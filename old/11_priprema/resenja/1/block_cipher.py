from poly import poly_inv

def toNibbles(W):
    return W >> 4, W & 0xf

def fromNibbles(N0, N1):
    return (N0 << 4) | N1

def S(N):
    return poly_inv(N, 0b10011) ^ 0b101

def SByte(W):
    N0, N1 = toNibbles(W)
    return fromNibbles(S(N0), S(N1))

def SBlock(B):
    return [SByte(B[0]), SByte(B[1])]

def R(W):
    N0, N1 = toNibbles(W)
    return fromNibbles(N1, N0)

def KSA(K0):
    W = [K0[0], K0[1], 0, 0, 0, 0, 0, 0]
    K = [K0]
    for i in range(1, 4):
        W[2*i]     = W[2*i - 2] ^ R(SByte(W[2*i - 1]))
        W[2*i + 1] = W[2*i - 1] ^ W[2*i]
        K.append([W[2*i], W[2*i+1]])
    return K

def P(B):
    N0, N1 = toNibbles(B[0])
    N2, N3 = toNibbles(B[1])
    return [fromNibbles(N3, N1), fromNibbles(N2, N0)]

def D(B, K):
    return [B[0] ^ K[0], B[1] ^ K[1]]

def encryptBlock(B, K):
    Ks = KSA(K)
    B = D(B, K)
    for i in range(1, 4):
        B = D(P(SBlock(B)), Ks[i])
    return B

def SInv(N):
    return poly_inv(N ^ 0b101, 0b10011)

def SInvByte(W):
    N0, N1 = toNibbles(W)
    return fromNibbles(SInv(N0), SInv(N1))

def SInvBlock(B):
    return [SInvByte(B[0]), SInvByte(B[1])]

def decryptBlock(B, K):
    Ks = KSA(K)
    for i in range(3, 0, -1):
        B = SInvBlock(P(D(B, Ks[i])))
    B = D(B, K)
    return B
