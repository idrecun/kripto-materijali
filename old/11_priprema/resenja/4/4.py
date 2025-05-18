import pohlig_hellman as ph

g = 3
p = 3748449900074770210591427759602449290611
A = 2171656519933921686726309257804235818783
r = 860883284086020753921032463243860692127
s = 1662926245658468968899623110514833541528
M1 = 123
M2 = 456

k = ph.pohlig_hellman(g, r, p)
# s = k^-1(M1 + a * r)
# k*s = M1 + a * r
# k*s - M1 = a * r
ar = (k * s - M1) % (p - 1)
s2 = (pow(k, -1, p - 1) * (M2 + ar)) % (p - 1)
print(f'({r}, {s2})')

## verify sig
print(pow(r, s2, p) == (pow(g, M2, p) * pow(A, r, p)) % p)
