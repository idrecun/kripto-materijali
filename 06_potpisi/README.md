# Asimetrična kriptografija 2: Digitalni potpisi i napadi

_Literatura: Cryptography made simple (poglavlje 15)_

Digitalni potpisi su kriptografski mehanizmi koji omogućavaju proveru autentičnosti
poruke i njenog pošiljaoca. Potpisi moraju biti:
- Nefalsifikujući (samo vlasnik privatnog ključa može da generiše validan potpis)
- Proverljivi (svako može da proveri validnost potpisa koristeći javni ključ)
- Vezani za poruku (potpis je validan samo za tu poruku)

## RSA digitalni potpisi

RSA se može koristiti i za digitalne potpise, efektivno zamenom operacija šifrovanja
i dešifrovanja.

~~~
Potpisivanje: s = m^d mod N
Verifikacija: m = s^e mod N
~~~

`rsa_sign.py` implementira RSA digitalne potpise.

## DSA (Digital Signature Algorithm)

DSA je standard za digitalne potpise zasnovan na DLP. Za razliku od RSA, potpisi
uključuju slučajan element.

~~~
Javni ključ: (p, q, g, y = g^x)
Privatni ključ: x

Potpisivanje:
1. Izabrati k
2. r = (g^k mod p) mod q
3. s = k^(-1)(H(m) + xr) mod q

Verifikacija:
1. u1 = s^(-1)H(m) mod q
2. u2 = s^(-1)r mod q
3. v = (g^u1 * y^u2 mod p) mod q
4. Proveriti v = r
~~~

`dsa.py` implementira DSA.

## Schnorr potpisi

Pojednostavljena verzija DSA. Schnorr potpisi su elegantni i efikasni.

~~~
Javni ključ: (p, q, g, y = g^x)
Privatni ključ: x

Potpisivanje:
1. Izabrati k
2. r = g^k mod p
3. e = H(m || r)
4. s = k + xe mod q

Verifikacija:
1. r' = g^s * y^(-e) mod p
2. e' = H(m || r')
3. Proveriti e = e'
~~~

`schnorr.py` implementira Schnorr potpise.

## Pohlig-Hellman napad

Napad na DLP koji radi efikasno kada je red grupe n = p1^e1 * ... * pk^ek proizvod
malih prostih stepena. Algoritam svodi DLP na više instanci u podgrupama manjeg reda.

~~~
Primer:
G = Z*_23, g = 5, h = 8
|G| = 22 = 2 * 11

1. Rešiti x mod 2
2. Rešiti x mod 11
3. Kombinovati rešenja kineskim teoremom o ostacima
~~~

`pohlig_hellman.py` implementira Pohlig-Hellman algoritam.

## Pollard p-1 napad

Napad na RSA koji radi efikasno kada je p-1 ili q-1 B-gladak broj (deljiv samo
prostim brojevima manjim od B).

~~~
Primer:
N = 1739
B = 5

1. a = 2
2. Računati a = a^i mod N za i = 2,3,4,5
3. d = gcd(a-1, N)
4. Ako je d netrivijalan, našli smo faktor

U ovom slučaju:
p = 37 (p-1 = 36 = 2^2 * 3^2)
q = 47 (q-1 = 46 = 2 * 23)
~~~

`pollard_p1.py` implementira Pollard p-1 algoritam. 