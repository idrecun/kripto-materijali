import pohlig_hellman

# Parametri Mesi-Omura kriptosistema
p=4961134016835065759021114081421108249451

# Razmenjeni sifrati
C1=1935806553456146246638434845968358334435
C2=2969866610933012757268798976814345183750
C3=4295774173108554255328476453966719136455

# Racunamo Bobanov kljuc za enkripciju
eb = pohlig_hellman.dlp(C1, C2, p)

# Racunamo Bobanov kljuc za dekripciju
db = pow(eb, -1, p - 1)

# Desifrujemo poruku
M = pow(C3, db, p)
print(M)
