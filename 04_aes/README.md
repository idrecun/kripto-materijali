# 04 AES

Implementacija (uprošćene) blok šifre
[AES](http://poincare.matf.bg.ac.rs/~ivan.drecun/kripto/skripta_zivkovic.pdf#page=27).

`poly.py` je pomoćna biblioteka koja realizuje operacije sa polinomima iz
[$\mathbb{Z}\_{2}[x]$](poincare.matf.bg.ac.rs/~ivan.drecun/kripto/skripta_zivkovic.pdf#page=24).
Polinom $b\_nx^n + \dots + b\_1x + b\_0$ predstavljen je brojem čiji je binarni
zapis $b\_n\dotsb\_1b\_0$. Sabiranje polinoma odgovara `xor` operaciji nad
njihovim reprezentacijama, na osnovu čega je moguće implementirati ostale
operacije. 
