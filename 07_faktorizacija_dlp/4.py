import pohlig_hellman

# Parametri El Gamal kriptosistema
g=3
p=1870481974960029238219966388771406118351

# Bobanov javni kljuc
B=1004333145870573517975149862105287178215

# Sifrat i Anin privremeni javni kljuc
C=1702744174218185477932013811228957311607
A=1314911118236658566754878896771289605934

# Racunamo Anin tajni kljuc
a = pohlig_hellman.dlp(g, A, p)

# Racunamo razmenjen kljuc
S = pow(B, a, p)

# Racunamo inverz od S i desifrujemo poruku
Sinv = pow(S, -1, p)
M = (C * Sinv) % p
print(M)
