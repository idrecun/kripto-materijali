# Kriptografija

Materijali za vežbe iz predmeta Kriptografija na master studijama.

## Podešavanje okruženja

Za pokretanje primera potrebno je Python 3.8 ili noviji i nekoliko dodatnih biblioteka.
Biblioteke se instaliraju u virtuelno okruženje (virtual environment) kako ne bi
došlo do konflikta sa sistemskim Python paketima.

### Inicijalno podešavanje

Pokrenite sledeću komandu da napravite virtuelno okruženje i instalirate potrebne
biblioteke:

```bash
make setup
```

Ova komanda će:
1. Napraviti virtuelno okruženje u direktorijumu `venv/`
2. Instalirati biblioteke navedene u `requirements.txt`:
   - `pycryptodome` - za kriptografske primitive
   - `Pillow` - za rad sa slikama
   - `sympy` - za matematičke operacije

### Aktiviranje okruženja

Pre pokretanja primera, potrebno je aktivirati virtuelno okruženje:

```bash
source venv/bin/activate
```

Nakon aktivacije, u prompt-u će se pojaviti `(venv)` prefiks koji označava da je
okruženje aktivno. Sada možete pokretati primere, na primer:

```bash
cd 01_klasicne_sifre
python caesar_enc.py
```

### Čišćenje

Ako želite da obrišete virtuelno okruženje i keširane fajlove:

```bash
make clean
```

## Struktura materijala

1. Klasične šifre
2. Protočne šifre
3. Blok šifre
4. Heš funkcije
5. Asimetrični kriptosistemi
6. Asimetrični potpisi
7. Eliptičke krive 