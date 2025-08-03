# Faktorizacija i problem diskretnog logaritma

Implementacije Polardovog p-1 algoritma za faktorizaciju i Polig-Helman algoritma za rešavanje problema
diskretnog logaritma. Oba algoritma se zasnivaju na pretpostavci da je broj $p-1$ $B$-gladak.

## Pohlig-Hellman napad

Napad na DLP koji radi efikasno kada je red grupe n = p1^e1 * ... * pk^ek proizvod
malih prostih stepena. Algoritam svodi DLP na više instanci u podgrupama manjeg reda.

`pohlig_hellman.py` implementira Pohlig-Hellman algoritam.

## Pollard p-1 napad

Napad na RSA koji radi efikasno kada je p-1 ili q-1 B-gladak broj (deljiv samo
prostim brojevima manjim od B).

`pollard_p1.py` implementira Pollard p-1 algoritam. 

## Zadaci

1. Ana Bobanu šalje poruku enkriptovanu pomoću RSA. Bobanov javni ključ je:
```
n=128012969945026248732835279448470961755200314723736138420211480647446338936601
e=45003644880317641650549332948458540440828733125352288665595332773107626216631
```
Odrediti poruku M ako je poznat šifrat:
```
C=17804263439160944615212115660102150497899902713732968130942328933737091348102
```

2. Bobanov javni RSA ključ je:
```
n=7603286354234243903435872704677498363399458016631578496018195845589487786172473
e=7535918899271596912605330771330141519800214292622992808169830647334620913196679
```
Predstaviti se lažno kao Boban i poslati Ani potpisanu poruku:
```
M=11111
```

3. Ana i Boban razmenjuju tajni ključ pomoću Difi-Helman protokola. Parametri su:
```
g=2
p=7601624022030852444912481695317914837957
```
Javni ključevi su:
```
A=4056414706808306835926218227089371088198
B=6496255164125604880472239459619844918400
```
Odrediti tajni ključ.

4. Ana Bobanu šalje poruku enkriptovanu pomoću El Gamal kriptosistema. Parametri su:
```
g=3
p=1870481974960029238219966388771406118351
```
Bobanov javni ključ je:
```
B=1004333145870573517975149862105287178215
```
Odrediti poruku M ukoliko su poznati šifrat i Anin privremeni javni ključ:
```
C=1702744174218185477932013811228957311607
A=1314911118236658566754878896771289605934
```