# Heš funkcije

_Literatura: Cryptography made simple (poglavlje 14)_

Heš funkcije su kriptografske primitive koje preslikavaju poruke proizvoljne
dužine u nizove bitova fiksne dužine. Fokusiraćemo se na konstrukcije heš
funkcija i njihove primene u kriptografiji.

## Svojstva heš funkcija

Heš funkcija $H$ mora da zadovolji sledeća svojstva:

1. **Preimage resistance** (one-way function): Za dato $y$ nije moguće naći $x$
   tako da je $H(x)=y$

2. **Second preimage resistance**: Za dato $x$ nije moguće naći $x' \neq x$
   tako da je $H(x)=H(x')$

3. **Collision resistance**: Nije moguće naći bilo koji par $x \neq x'$ tako da
   je $H(x)=H(x')$

U ovom kontekstu "nije moguće" znači da ne postoji algoritam koji može da izračuna
traženi rezultat u bilo kom razumnom vremenu.

## Proširenje poruke (padding)

Pre primene heš funkcije, poruku je potrebno proširiti do određene dužine, u
zavisnosti od toga kako je heš funkcija konstruisana. Postoji više načina da se
to uradi:

~~~
Poruka: 1011
Dužina poruke: 4 bita
Dužina bloka: 8 bitova

0* pad:      1011 0000
10* pad:     1011 1000
10*||Len:    1011 1000 0000 0100
0*||Len:     1011 0000 0000 0100
10*1 pad:    1011 1001
~~~

## Konstrukcije heš funkcija

### Merkle-Damgard konstrukcija

Merkle-Damgard konstrukcija omogućava konstrukciju heš funkcije za datu
funkciju $f$. Funkcija $f$ preslikava blok poruke i stanje heš funkcije u
naredno stanje.

$
s_0 = IV \\
s_i = f(m_i || s_{i-1}) \\
H(m) = s_n
$

`md.py` implementira Merkle-Damgard konstrukciju. Za funkciju $f$ koristi se
jednostavna SP mreža.

### Sponge konstrukcija

Sponge konstrukcija je fleksibilnija od Merkle-Damgard konstrukcije. Koristi
bijekciju $f$ i deli stanje na dva dela, $s=[r|c]$. $r$ je deo koji se direktno
kombinuje sa ulaznom porukom i iz kog se izvlači heš vrednost, a $c$ je
kapacitet koji predstavlja unutrašnje stanje heša.

Heš funkcija se dobija tako što se prvo "upija" poruka, odnosno tako što se
svaki blok poruke XOR-uje sa trenutnim $r$. Između svaka dva bloka se stanje
$[r|c]$ transformiše funkcijom $f$. Nakon upijanja svih blokova, vrednost heš
funkcije se "istiskuje", odnosno čitaju se blokovi iz $r$ do željene dužine heš
vrednosti.

`sponge.py` implementira Sponge konstrukciju. Za funkciju $f$ koristi se
jednostavna SP mreža.

## Primene heš funkcija za konstrukciju MAC i KDF

### HMAC (Hash-based Message Authentication Code)

HMAC omogućava proveru autentičnosti poruke korišćenjem heš funkcije i tajnog
ključa. Jednostavna konstrukcija $MAC(m,k)=H(k||m)$ nije bezbedna za
Merkle-Damgard heševe, pa se koristi:

$HMAC(m,k) = H(k_2 || H(k_1 || m))$

gde je $k_1 = k \oplus ipad$, $k_2 = k \oplus opad$ za konstante $ipad$ i
$opad$.

Vrednost $v=HMAC(c,k)$ se šalje uz šifrat $c=E(m,k)$. Provera autentičnosti
primljene poruke se vrši tako što se izračuna $HMAC(c,k)$ i uporedi sa
primljenom vrednošću $v$.

### KDF (Key Derivation Function)

KDF služi za izvođenje kriptografskog ključa iz lozinke ili drugih tajnih
vrednosti. Na primer, ako blok šifra očekuje ključ dužine 128 bita, a lozinka
je dužine 64 bita, potrebno je izvesti ključ dužine 128 bita. Takođe, izvedeni
ključ će imati poželjna statistička svojstva koja lozika uglavnom nema. Jedna
konstrukcija KDF korišćenjem heš funkcije je:

$KDF(k) = H(k||n-1) || ... || H(k||0)$

### Sponge konstrukcije za MAC i KDF

Sponge konstrukcija je veoma fleksibilna i može se prilagoditi za izračunavanje MAC i KDF:

- MAC možemo računati kao $H(k||m)$
- KDF možemo dobiti upijanjem lozinke $m$ i istiskivanjem $k$ do željene dužine ključa
