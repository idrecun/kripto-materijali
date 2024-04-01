# 01 Klasične šifre

## One-Time Pad (OTP)
- `otp_enc_text.py` Implementacija šifrovanja teksta.
- `otp_dec_text.py sifrat1.txt sifrat2.txt` Implementacija razbijanja šifrovanog teksta.
    1. Šifrovati poruke `hello world, i like programming` i `i enjoy programming, hello matf` ključem `key`.
    2. Sačuvati šifrate u fajlove `sifrat1.txt` i `sifrat2.txt`.
    3. Razbiti šifru.
- `otp_enc_img.py slika.jpg` Implementacija šifrovanja slike.
- `otp_dec_img.py sifrat1.png sifrat2.png` Implementacija razbijanja šifrovanih slika.
    1. Enkriptovati slike iz `assets/` bez prikazivanja slika.
    2. Prikazati šifrate.
    3. Dekriptovati i pokazati rezultat.
    4. Pokazati originalne slike.

## Cezar
- `caesar_enc.py [poruka.txt]` Implementacija šifrovanja teksta.
- `caesar_dec.py [sifrat.txt]` Implementacija razbijanja šifrovanog teksta.
    1. Šifrovati `paragraf.txt` ključem `k`.
    2. Razbiti šifru `caesar.txt`.

## Vigenere
- `vigenere_enc.py [poruka.txt]` Implementacija šifrovanja teksta.
- `vigenere_dec_dictionary.py [sifrat.txt]` Implementacija razbijanja šifrovanog teksta.
- `vigenere_dec_frequency.py [sifrat.txt]` Implementacija razbijanja šifrovanog teksta.
    1. Šifrovati `paragraf.txt` ključem `key`.
    2. Razbiti šifru `vigenere.txt` napadom pomoću rečnika.
    3. Razbiti šifru `vigenere.txt` frekvencijskim napadom.
