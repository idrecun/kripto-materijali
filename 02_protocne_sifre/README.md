# Protočne šifre

_Literatura: Cryptography made simple, poglavlje 12_

Moderne protočne šifre zasnivaju se na generisanju pseudoslučajnog niza bitova
na osnovu datog ključa, koji se na neki način kombinuje sa porukom (uglavnom
XOR operacijom) radi šifrovanja. Fokusiraćemo se na konstrukciju protočne šifre
zasnovanu na linearnim povratnim shift registrima.

## LFSR

Linearni povratni shift registar (LFSR - linear feedback shift register) drži
stanje od n bitova $s_1, \dots, s_n$. Svaki naredni bit pseudoslučajnog stanja
računa se po formuli $s_{i} = c_n s_{i - n} + \dots + c_1 s_{i-1}$ gde je $+$
operacija XOR, $c_1, \dots, c_n$ su bitovi koji definišu registar i služe da
odaberu bitove stanja na osnovu kojih se računa naredni bit stanja.

Na primer, neka je LFSR dužine $n=4$ definisan sa $c=[1, 0, 1, 1]$. To znači da
se naredni bit stanja računa po formuli $s_i = s_{i-4} + s_{i-3} + s_{i-1}$.

~~~
 ┌──>s[i-1] s[i-2] s[i-3] s[i-4]
 │     │             │      │
 └───[          XOR          ]───> output
~~~

Ako je početno stanje $s_{i-1}, s_{i-2}, s_{i-3}, s_{i-4} = 1, 0, 0, 0$, prvih
nekoliko koraka generisanja bitova izgleda ovako:

~~~
 1 0 0 0
 |   | |
 +---+-+-> 1

 1 1 0 0
 |   | |
 +---+-+-> 1

 1 1 1 0
 |   | |
 +---+-+-> 0

 0 1 1 1
 |   | |
 +---+-+-> 0

 0 0 1 1
 |   | |
 +---+-+-> 0
~~~

`lfsr.py` implementira LFSR.

`bits.py` implementira pomoćne funkcije za rad sa nizvima bitova.

`lfsr_cipher.py` implementira protočnu šifru zasnovanu na LFSR. Poruka se
šifruje poput OTP-a, XOR-ovanjem sa generisanim nizom bitova. Dešifrovanje se
radi na isti način.

## NLFSR

LFSR generator nije pogodan za kriptografske primene. Pretpostavimo da je
poznato $2n$ uzastopnih bitova generisanih LFSR generatorom dužine $n$. Moguće
je odrediti parametre generatora i sve generisane bitove rešavanjem linearnog
sistema. (_strana 231_)

`lfsr_break.py` implementira određivanje parametara LFSR na osnovu $2n$
generisanih bitova.

Kako bismo napravili otporan kriptosistem, kombinujemo više LFSR na nelinearan
način.

### Shrinking generator

`shrinking_generator.py` implementira jedan takav NLFSR. Koriste se dva LFSR. U
svakom koraku pomeramo oba generatora za jedan. Ukoliko prvi generator vrati 1,
na izlaz NLFSR generatora ispisujemo bit drugog generatora. Ako prvi generator
vrati 0, bit drugog generatora se preskače.

~~~
 [LFSR A]───────┐
 [LFSR B]──[if A = 1]──> output

Primer:
 A: 0110101110
 B: 1010011100
 O:  01 0 110
~~~

### Alternating step generator

`alternating_step.py` implementira NLFSR koji koristi tri LFSR generatora.
Kontrolni generator se pomera u svakom koraku. U zavisnosti od toga da li je
generisao 0 ili 1 bira se koji od druga dva LFSR generatora se pomera. Na izlaz
NLFSR se ispisuje XOR izlaznih bitova drugog i trećeg LFSR (u XOR se koristi
poslednji generisan bit generatora koji nije pomeren).

~~~
 [LFSR C]─┬─[LFSR A, clock if C = 0]─[XOR]─> output
          └─[LFSR B, clock if C = 1]───┘

Primer:
 C:  01100011
 A: 01..011..
 B: 1.01...01
 O:  01010010
~~~
