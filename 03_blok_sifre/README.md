# Blok šifre

_Literatura: Cryptography made simple (poglavlje 13)_

Blok šifre su kriptografski sistemi koji šifruju podatke u blokovima fiksne veličine
(najčešće 64 ili 128 bitova). Za fiksiran ključ, blok šifra je bijekcija na skupu
$\{0,1\}^k$ gde je $k$ veličina bloka. Prikazaćemo dva načina za konstrukciju blok
šifri: Feistel mreže i SP mreže.

## Osnovne komponente

### S-box (Substitution box)

S-box je komponenta koja vrši supstituciju - preslikava m ulaznih bitova u n
izlaznih bitova, najčešće pomoću unapred definisane lookup tabele.

~~~
Primer:
4 bita -> 3 bita (prvi bit određuje red, preostala tri kolonu)

  │ 0 1 2 3 4 5 6 7
──┼────────────────
0 │ 6 0 1 7 2 4 5 3
1 │ 7 6 5 3 0 1 4 2

S(3)  = 7 (jer je 3 = 0.011)
S(13) = 1 (jer je 13 = 1.101)
~~~

### P-box (Permutation box)

P-box vrši permutaciju bitova - preslikava m ulaznih bitova u n izlaznih bitova
promenom njihovog redosleda. P-box može da:

Permutuje (n->n bitova)

~~~
0 1 1 1 0 1 0 1
│ │ │ │ │ │ │ │ 
0 1 2 3 4 5 6 7
[    P-box    ]
3 2 7 6 1 0 5 4
│ │ │ │ │ │ │ │ 
1 1 1 0 1 0 1 0
~~~

Proširi (n->m bitova, m>n)

~~~
 0   0   1   0
 │   │   │   │
 0   1   2   3
[    P-box    ]
0 1 2 3 3 2 1 0
│ │ │ │ │ │ │ │ 
0 0 1 0 0 1 0 0
~~~

- Kompresuje (n->m bitova, m<n)

~~~
1 1 1 0 0 1 1 0
│ │ │ │ │ │ │ │ 
0 1 2 3 4 5 6 7
[    P-box    ]
 0   2   4   6
 │   │   │   │
 1   1   0   1
~~~

`symmetric.py` impelmentira S-box i P-box primitive.

## Feistel mreže

Feistel mreža je konstrukcija koja omogućava da od proizvoljne funkcije
enkripcije $F(M, K)$ formiramo blok šifru. Blok se deli na dva dela, $B=[L |
R]$. U jednoj rundi Feistel mreže se blok transformiše po formuli $[L | R] \to
[R | L ⊕ F(R, K)]$. U svakoj rundi se koristi ključ runde $K_i$, koji je na
neki način izveden od početnog ključa $K$.

`feistel.py` implementira Feistel mrežu.

DES je kriptosistem zasnovan na Feistel konstrukciji. Koristi 16 rundi, a funkcija
$F$ je definisana kombinovanjem S-box-eva i P-box-a.

## SP (Substitution-Permutation) mreže

Slično Feistel mreži, SP mreža se odvija u više rundi. Jedna runda SP mreže se
sastoji od primene S-box-a i P-box-a. U svakoj rundi se koristi ključ runde
$K_i$, a runda se odvija u tri koraka:

1. Blok i ključ runde se XOR-uju
2. Primenjuje se S-box
3. Primenjuje se P-box

Za razliku od Feistel mreže gde $F$ može biti proizvoljno, u SP mreži je
neophodno da svi S-box-ovi i P-box-ovi budu bijekcije. To je potrebno kako bi
dešifrovanje bilo moguće. Dešifrovanje se vrši tako što se primenjuju inverzne
operacije u obrnutom redosledu.

`spn.py` implementira SP mrežu.

AES je primer blok šifre konstruisane kao SP mreža.

## Operacioni modovi

Prikazane konstrukcije blok šifri omogućavaju šifrovanje blokova fiksne dužine.
Operacioni modovi služe da omoguće šifrovanje poruka proizvoljne dužine korišćenjem
blok šifri.

`modes.py` implementira različite operacione modove.

### ECB (Electronic Code Book)

Svaki blok se šifruje nezavisno. Problem sa ovim modom je što se isti blokovi
šifruju u isti šifrat.

$c_i = E(m_i)$

### CBC (Cipher Block Chaining)

Svaki blok se XOR-uje sa prethodnim šifratom i tako enkriptuje, dok se prvi
blok XOR-uje sa inicijalizacijom vektorom $IV$.

$c_i = E(m_i ⊕ c_{i-1})$

### OFB (Output Feedback)

Pretvara blok šifru u protočnu šifru time što generiše niz blokova $y$, počevši
od $y_0=IV$.

$
y_i = E(y_{i-1}) \\
c_i = m_i ⊕ y_i
$

### CFB (Cipher Feedback)

Slično OFB-u ali koristi prethodni šifrat, počevši od $c_0=IV$.

$c_i = m_i ⊕ E(c_{i-1})$

### CTR (Counter)

Moderan operacioni mod koji pretvara blok šifru u protočnu, ali takođe i
omogućava paralelizaciju. Ideja je da se blokovi generišu kao šifrati brojeva
1, 2, 3, itd. redom. U ovom modu neophodno je da se nikad ne ponovi redni broj
koji se šifruje istim ključem. Dodajemo vrednost $n$ koja garantuje da će
šifrovanje svake naredne poruke započeti od vrednosti koja je veća od svih
prethodnih.

$
y_i = E(n + i) \\
c_i = m_i ⊕ y_i
$

Recimo da je za šifrovanje prve poruke bilo potrebno šifrovati 3 bloka i da smo
počeli od $n=0$. Dakle, za šifrovanje smo koristili $E(0), E(1), E(2)$. Za
sledeću poruku moramo uzeti $n \geqslant 3$ kako bismo krenuli šifrovanje od
$E(3)$ i ne bismo ni jedan od prethodnih blokova ponovo koristili.

