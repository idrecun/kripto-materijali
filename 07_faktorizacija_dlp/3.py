import pohlig_hellman

# Parametri DH razmene
g=2
p=7601624022030852444912481695317914837957

# Javni kljucevi
A=4056414706808306835926218227089371088198
B=6496255164125604880472239459619844918400

# Racunamo Anin tajni kljuc
a = pohlig_hellman.dlp(g, A, p)

# Racunamo razmenjen kljuc
S = pow(B, a, p)
print(S)
