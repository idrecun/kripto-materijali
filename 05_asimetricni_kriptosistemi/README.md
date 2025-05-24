# Kriptografija javnog ključa

_Literatura: Cryptography made simple (poglavlja 2, 3, 15, 16)_

Asimetrična kriptografija (kriptografija javnog ključa) rešava problem
distribucije ključeva koji postoji u simetričnoj kriptografiji. Umesto deljenja
tajnog ključa, svaki učesnik ima par ključeva - javni ključ koji se slobodno
distribuira i privatni ključ koji se čuva u tajnosti.

Bezbednost asimetričnih kriptosistema zasniva se na postojanju "trapdoor"
funkcija. To su funkcije koje je lako izračunati u jednom smeru, ali je teško
naći inverznu vrednost bez dodatne "trapdoor" informacije.

## Problem diskretnog logaritma (DLP)

Za date vrednosti $g$ i $h$ u cikličnoj grupi $G$ reda $n$, problem je pronaći $x$ tako da
je $g^x = h$. Ovaj problem je težak u određenim grupama (npr. $(\mathbb{Z}, \cdot)$), 
ali može biti i lak (npr. $(\mathbb{Z},+)$).

~~~
Primer:
G = Z*_23, g = 5
h = 8

Naći x tako da je 5^x ≡ 8 (mod 23)

Rešenje je x = 18 jer je:
5^18 ≡ 8 (mod 23)
~~~

## Problem faktorizacije

Za dat složen broj $N$, problem je pronaći njegove proste činioce. Ovaj problem je težak za dovoljno velike brojeve.

~~~
Primer:
N = 77

Faktorizacija:
77 = 7 * 11
~~~

### Diffie-Hellman razmena ključa (`diffie-hellman/`)

Omogućava zajedničko generisanje ključa koji se posle može koristiti za
enkripciju simetričnim kriptosistemima. Bezbednost je zasnovana na DLP.

Svaki učesnik generiše svoj privatni podatak (npr. $a$) i na osnovu njega
računa svoj javni podatak ($A=g^a$). Javni podatak šalje drugom učesniku.
Obe strane mogu da izračunaju isti, zajednički ključ kombinovanjem svog
privatnog podatka i javnog podataka drugog učesnika, npr. $K=B^a=g^{ab}$.
Sve operacije se vrše po modulu prostog broja $p$. Pretpostavka je da su
$g$ i $p$ javni, unapred određeni parametri protokola.

~~~
       (privatno a)    A = g^a    ───A──>     (privatno b)
                      <───B───    B = g^b
    K = B^a = g^(ab)                     K = A^b = g^(ab)
~~~

- `diffie_hellman.py` - implementacija DH protokola
- `client.py` i `server.py` - primer upotrebe za razmenu šifrovanih poruka

### ElGamal kriptosistem (`elgamal/`)

Kriptosistem zasnovan na DLP. Šifrovanje poruke uključuje slučajan element, tako
da jedna ista poruka može imati različite šifrate.

Slično Difi-Helman razmeni ključa, parametri $p$ i $g$ su javni, unapred određeni
parametri. Pošiljalac generiše svoj privatni ključ $x$, i na osnovu njega generiše
svoj javni ključ $h=g^x$. Poruka $m$ se šifruje kombinovanjem sa slučajnim elementom
$y$ i ta dva podatka se šalju kao zamaskirani $c_1=g^y$ i $c_2=m \cdot h^y$.

~~~
Javni parametri: p, g
Javni ključ: h = g^x
Privatni ključ: x

m ──> Izabrati y          ───(c1,c2)──>    c1 = g^y
      c1 = g^y                             c2 = m * h^y
      c2 = m * h^y                         m = c2 * (c1^x)^(-1)
~~~

- `elgamal.py` - implementacija ElGamal kriptosistema
- `client.py` i `server.py` - primer šifrovanja i dešifrovanja poruka

### RSA kriptosistem (`rsa/`)

RSA je kriptosistem zasnovan na problemu faktorizacije. Za razliku od ElGamal
kriptosistema, prosti brojevi $p$ i $q$ su tajni parametri koje korisnik generiše na
slučajan način prilikom generisanja privatnog ključa. Privatni ključ je slučajno
odabrana vrednost $e$, a javni ključ se sastoji od dva podatka, $\phi(N) = (p-1)(q-1)$
i $d = e^{-1} \pmod{\phi(N)}$.

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

Svaki protokol ima implementiran primer komunikacije između klijenta i servera.
Za pokretanje (npr. za `rsa/`):

1. U jednom terminalu pokrenuti server:
   ```
   cd rsa/
   python3 server.py
   ```

2. U drugom terminalu pokrenuti klijent:
   ```
   cd rsa/
   python3 client.py
   ```