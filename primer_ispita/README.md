## Primer zadataka za ispit

U svakom zadatku je potrebno dopuniti postojeću implementaciju. Delovi koje je
potrebno implementirati označeni su `TODO` komentarima. Rešenja zadataka nalaze
se neposredno iza tih komentara. Na ispitu će biti dostupni svi delovi
implementacije izuzev traženih `TODO` segmenata.

### 1) Implementirati LFSR generator.

### 2) Implementirati Feistel blok šifru u ECB modu. Funkcija `F` je data u `2/feistel.py`.

### 3) Implementirati protokol komunikacije između klijenta i servera (RSA enkripcija celobrojnog m):
- Server šalje svoj javni ključ klijentu.
- Klijent generiše ključeve i šalje ih serveru.
- Klijent priprema ceo broj `m`, šifruje ga serverovim javnim ključem i šalje tako šifrovan broj serveru.
- Server dešifruje poruku svojim privatnim ključem.
- Server formira odgovor `m' = m + 1`, šifruje ga klijentovim javnim ključem i šalje ga klijentu.
- Klijent dešifruje `m'` i ispisuje rezultat.

### 4) Implementirati Difi-Helman razmenu ključa nad eliptičkim krivama. Dopuniti implementaciju operacije sabiranja tačaka na eliptičkoj krivoj.
