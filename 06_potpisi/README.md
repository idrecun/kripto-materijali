# Digitalni potpisi

_Literatura: Cryptography made simple (poglavlja 2, 3, 16)_

Digitalni potpisi su kriptografski protokoli koji omogućavaju proveru autentičnosti
poruke i njenog pošiljaoca. Potpisi moraju biti:
- Nefalsifikujući (samo vlasnik privatnog ključa može da generiše validan potpis)
- Proverljivi (svako može da proveri validnost potpisa koristeći javni ključ)
- Vezani za poruku (potpis je validan samo za tu poruku)

## RSA digitalni potpisi

RSA se može koristiti i za digitalne potpise. Privatni ključ se može koristiti za potpisivanje poruke, a javni ključ za proveru potpisa. Kao i u ostalim algoritmima digitalnog potpisivanja, umesto cele poruke m potpisuje se njena heš vrednost.

~~~
Potpisivanje: s = m^d mod N
Verifikacija: m = s^e mod N
~~~

`rsa_sign.py` implementira RSA digitalne potpise.

## Šnorov potpis

Parametri Šnorovog potpisa su broj p, element g iz Zp i prost broj q koji
odgovara velicini podgrupe od Zp generisane elementom g. Privatni ključ za
potpisivanje je slučajan broj x mod q, a javni ključ je y = g^x mod q. Prilikom
potpisivanja poruke se koristi slučajan element k. Neophodno je da taj element
zaista bude generisan slučajno i na nepredvidiv način, jer bi u suprotnom bilo
moguće izvući privatni ključ iz potpisa.

~~~
Javni parametri: p, q, g
Privatni ključ: x
Javni ključ: y = g^x mod q

Potpisivanje:
1. Izabrati slučajno k
2. r = g^k mod p
3. e = H(m || r)
4. s = k + xe mod q
Potpis poruke m je par (e, s).

Verifikacija:
1. r' = g^s * y^(-e) mod p
2. e' = H(m || r')
3. Proveriti e = e'
~~~

`schnorr.py` implementira Šnorov potpis.

## DSA (Digital Signature Algorithm)

Parametri i pretpostavke DSA potpisa su iste kao za Šnorove potpise.

~~~
Javni parametri: p, q, g
Privatni ključ: x
Javni ključ: y = g^x mod q

Potpisivanje:
1. Izabrati slučajno k
2. r = (g^k mod p) mod q
3. s = k^(-1)(H(m) + xr) mod q
Potpis poruke m je par (r, s)

Verifikacija:
1. u1 = s^(-1)H(m) mod q
2. u2 = s^(-1)r mod q
3. v = (g^u1 * y^u2 mod p) mod q
4. Proveriti v = r
~~~

`dsa.py` implementira DSA.