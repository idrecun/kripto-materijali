import pollard_p1

# Bobanov javni kljuc
n=128012969945026248732835279448470961755200314723736138420211480647446338936601
e=45003644880317641650549332948458540440828733125352288665595332773107626216631

# Sifrat
C=17804263439160944615212115660102150497899902713732968130942328933737091348102

# Racunamo proste p i q takve da je n=pq
p = pollard_p1.factorize(n)
q = n // p

# Racunamo vrednost Ojlerove funkcije od n
phi = (p - 1) * (q - 1)

# Racunamo Bobanov privatni kljuc kao inverz javnog mod phi
d = pow(e, -1, phi)

# Desifrujemo poruku
M = pow(C, d, n)
print(M)
