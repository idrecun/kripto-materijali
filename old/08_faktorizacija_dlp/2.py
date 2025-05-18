import pollard_p1

# Bobanov javni kljuc
n=7603286354234243903435872704677498363399458016631578496018195845589487786172473
e=7535918899271596912605330771330141519800214292622992808169830647334620913196679

# Poruka
M=11111

# Racunamo proste p i q takve da je n=pq
p = pollard_p1.factorize(n)
q = n // p

# Racunamo vrednost Ojlerove funkcije od n
phi = (p - 1) * (q - 1)

# Racunamo Bobanov privatni kljuc kao inverz javnog mod phi
d = pow(e, -1, phi)

# Potpisujemo poruku
S = pow(M, d, n)
print(S)

# Proveravamo potpis
print(pow(S, e, n) == M)
