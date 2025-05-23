# Eliptičke krive

_Literatura: Cryptography made simple (poglavlje 15)_

Eliptičke krive su matematičke strukture koje se koriste za konstrukciju kriptografskih
protokola. Kriva je definisana jednačinom $y^2 = x^3 + ax + b$ nad poljem $\mathbb{F}_p$,
gde su $a$ i $b$ parametri krive. Tačke na krivoj, zajedno sa specijalnom tačkom u
beskonačnosti $\mathcal{O}$, čine grupu sa operacijom sabiranja.

## Operacije nad tačkama

### Sabiranje tačaka

Neka su $P=(x_1,y_1)$ i $Q=(x_2,y_2)$ tačke na krivoj. Njihov zbir $R=P+Q=(x_3,y_3)$
se računa na sledeći način:

- Ako je $P=\mathcal{O}$, onda je $R=Q$
- Ako je $Q=\mathcal{O}$, onda je $R=P$
- Ako je $P=-Q$ (tj. $x_1=x_2$ i $y_1=-y_2$), onda je $R=\mathcal{O}$
- Inače:
  - Ako je $P \neq Q$: $s = (y_2-y_1)/(x_2-x_1)$
  - Ako je $P = Q$: $s = (3x_1^2 + a)/(2y_1)$
  - $x_3 = s^2 - x_1 - x_2$
  - $y_3 = s(x_1-x_3) - y_1$

### Množenje skalarom

Množenje tačke skalarom $k$ se definiše kao uzastopno sabiranje: $kP = P + P + \dots + P$
($k$ puta). U praksi se koristi efikasniji double-and-add algoritam:

~~~
k = 13 = 1101₂
P = G

13G = G + 4G + 8G

1. G
2. 2G = G+G
3. 4G = 2G+2G
4. 5G = 4G+G
5. 8G = 4G+4G
6. 13G = 8G+5G
~~~

`ec.py` implementira osnovne operacije nad eliptičkim krivama. Koristi se kriva secp256k1
sa parametrima:

~~~
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0
b = 7
G = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
     0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141  # red tačke G
~~~

## Kriptografski protokoli

### Diffie-Hellman razmena ključeva (`diffie_hellman/`)

Diffie-Hellman protokol omogućava razmenu tajnog ključa preko nesigurnog kanala:

1. Alice generiše privatni ključ $a$ i šalje Bob-u javni ključ $A=aG$
2. Bob generiše privatni ključ $b$ i šalje Alice javni ključ $B=bG$
3. Oboje računaju zajednički ključ $K=abG$ (Alice kao $aB$, Bob kao $bA$)

### ElGamal šifrovanje (`elgamal/`)

ElGamal šema omogućava asimetrično šifrovanje poruka. Poruka $m$ se prvo enkodira
kao tačka $M$ na krivoj. Šifrovanje:

1. Bob ima privatni ključ $b$ i javni ključ $B=bG$
2. Alice generiše slučajan $k$ i računa:
   - $R = kG$
   - $S = kB$ (zajednički ključ)
   - $C = M + S$ (šifrat)
3. Alice šalje Bob-u par $(R,C)$

Bob dešifruje računajući $M = C - bR$ (jer je $bR = bkG = kB = S$).

### EC-DSA digitalni potpisi (`ec-dsa/`)

EC-DSA je varijanta DSA algoritma nad eliptičkim krivama. Za potpisivanje poruke $m$:

1. Generišemo slučajan $k$
2. Računamo $R = kG$ i uzimamo $r = x_R \bmod n$
3. Računamo $s = k^{-1}(H(m) + dr) \bmod n$ gde je $d$ privatni ključ
4. Potpis je par $(r,s)$

Verifikacija potpisa $(r,s)$ za poruku $m$ i javni ključ $Q=dG$:

1. Računamo $w = s^{-1} \bmod n$
2. Računamo $u_1 = H(m)w \bmod n$ i $u_2 = rw \bmod n$
3. Računamo $R = u_1G + u_2Q$
4. Potpis je validan ako je $x_R \bmod n = r$

### Schnorr digitalni potpisi (`schnorr/`)

Schnorr potpisi su jednostavniji od EC-DSA. Za potpisivanje poruke $m$:

1. Generišemo slučajan $k$
2. Računamo $R = kG$
3. Računamo $e = H(R||Q||m)$ gde je $Q$ javni ključ
4. Računamo $s = k + ed \bmod n$ gde je $d$ privatni ključ
5. Potpis je par $(R,s)$

Verifikacija potpisa $(R,s)$ za poruku $m$ i javni ključ $Q$:

1. Računamo $e = H(R||Q||m)$
2. Proveravamo da li je $sG = R + eQ$

## Usage

Each protocol directory contains:
1. Core implementation file with the cryptographic functions
2. `client.py` and `server.py` demonstrating protocol usage
3. Uses the `network.py` module for client/server communication

To run the examples:
1. Start the server: `python server.py`
2. In another terminal, start the client: `python client.py`

The examples demonstrate key exchange, encryption/decryption, or signature generation/verification depending on the protocol.

