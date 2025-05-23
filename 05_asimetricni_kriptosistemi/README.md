# Kriptografija javnog ključa

_Literatura: Cryptography made simple (poglavlje 14)_

Asimetrična kriptografija, poznata i kao kriptografija javnog ključa, rešava problem
distribucije ključeva koji postoji u simetričnoj kriptografiji. Umesto deljenja tajnog
ključa, svaki učesnik ima par ključeva - javni ključ koji se slobodno distribuira i
privatni ključ koji se čuva u tajnosti.

Bezbednost asimetričnih kriptosistema zasniva se na postojanju jednosmernih funkcija
sa tajnim vratima. To su funkcije koje je lako izračunati u jednom smeru, ali je
teško naći inverznu vrednost bez dodatne informacije (tajnih vrata).

## Problem diskretnog logaritma (DLP)

Za date vrednosti g i h u cikličnoj grupi G reda n, problem je pronaći x tako da je
g^x = h. Ovaj problem se smatra računski teškim u određenim grupama.

~~~
Primer:
G = Z*_23, g = 5
h = 8

Naći x tako da je 5^x ≡ 8 (mod 23)

Rešenje je x = 18 jer je:
5^18 ≡ 8 (mod 23)
~~~

## Problem faktorizacije

Za dat složen broj N, problem je pronaći njegove proste činioce. Ovaj problem se
smatra računski teškim za dovoljno velike brojeve.

~~~
Primer:
N = 77

Faktorizacija:
77 = 7 * 11
~~~

## Implementacije protokola

U direktorijumu se nalaze implementacije tri protokola, svaki u svom poddirektorijumu:

### Diffie-Hellman protokol (`diffie-hellman/`)

Protokol za razmenu ključeva preko nesigurnog kanala. Bezbednost se zasniva na DLP.

~~~
       (privatno a)    A = g^a    ───A──>     (privatno b)
                      <───B───    B = g^b
    K = B^a = g^(ab)                     K = A^b = g^(ab)
~~~

- `diffie_hellman.py` - implementacija DH protokola
- `client.py` i `server.py` - primer upotrebe za razmenu šifrovanih poruka

### ElGamal kriptosistem (`elgamal/`)

Kriptosistem zasnovan na DLP. Šifrovanje poruke uključuje slučajan element, tako da
isto otvoreno pismo može imati različite šifrate.

~~~
Javni ključ: (p, g, h = g^x)
Privatni ključ: x

m ──> Izabrati y          ───(c1,c2)──>    c1 = g^y
      c1 = g^y                             c2 = m * h^y
      c2 = m * h^y                         m = c2 * (c1^x)^(-1)
~~~

- `elgamal.py` - implementacija ElGamal kriptosistema
- `client.py` i `server.py` - primer šifrovanja i dešifrovanja poruka

### RSA kriptosistem (`rsa/`)

Kriptosistem zasnovan na problemu faktorizacije. Za razliku od ElGamal-a, šifrovanje
je determinističko.

~~~
Generisanje ključeva:
1. Izabrati proste brojeve p, q
2. N = p * q
3. φ(N) = (p-1)(q-1)
4. Izabrati e tako da je gcd(e, φ(N)) = 1
5. Izračunati d tako da je e*d ≡ 1 (mod φ(N))

Javni ključ: (N, e)
Privatni ključ: (p, q, d)

Šifrovanje: c = m^e mod N
Dešifrovanje: m = c^d mod N
~~~

- `rsa.py` - implementacija RSA kriptosistema
- `client.py` i `server.py` - primer šifrovanja i dešifrovanja poruka

## Pokretanje primera

Svaki protokol ima implementiran primer komunikacije između klijenta i servera. Za pokretanje:

1. U jednom terminalu pokrenuti server:
   ```
   cd protokol/
   python server.py
   ```

2. U drugom terminalu pokrenuti klijent:
   ```
   cd protokol/
   python client.py
   ```

Gde je `protokol/` jedan od direktorijuma: `diffie-hellman/`, `elgamal/` ili `rsa/`.