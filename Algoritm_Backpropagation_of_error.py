import numpy as np

# Functia de activare bipolara si derivata acesteia
def activare_bipolara(x):
    return 2 / (1 + np.exp(-x)) - 1

def derivata_bipolara(x):
    return 0.5 * (1 + x) * (1 - x)

# Pattern-urile de intrare (z1, z2, z3) si iesirile dorite (d)
patternuri = np.array([
    [45, 48, 40],
    [50, 43, 41],
    [49, 50, 40],
    [50, 40, 39],
    [193, 195, 41],
    [200, 193, 40],
    [197, 194, 39],
    [200, 43, 40]
])

iesiri_dorite = np.array([1, 1, 1, 1, -1, -1, -1, -1])

# Normalizam pattern-urile de intrare
patternuri = patternuri / 200.0

# Adaugam coloana pentru bias manual
bias = np.ones((patternuri.shape[0], 1))
patternuri = np.concatenate((patternuri, bias), axis=1)

# Parametrii retelei
nr_intrari = 3
nr_ascunse = 3
nr_iesiri = 1
rata_instruire = 0.5
eroare_tolerata = 0.01
epoci_maxime = 500

# Initializam greutatile cu valori aleatoare
np.random.seed(0)
greutati_intrare_ascuns = np.random.uniform(-1, 1, (nr_intrari + 1, nr_ascunse))
greutati_ascuns_iesire = np.random.uniform(-1, 1, (nr_ascunse + 1, nr_iesiri))

# Instruire
epoca = 0  # Inițializăm epoca
for epoca in range(epoci_maxime):
    eroare_totala = 0

    for i in range(len(patternuri)):
        # Pas inainte
        intrare = patternuri[i]
        iesire_ascuns = activare_bipolara(np.dot(intrare, greutati_intrare_ascuns))
        iesire_ascuns = np.append(iesire_ascuns, 1)  # Bias la stratul ascuns
        iesire_finala = activare_bipolara(np.dot(iesire_ascuns, greutati_ascuns_iesire))

        # Calculam eroarea
        eroare = iesiri_dorite[i] - iesire_finala
        eroare_totala += eroare**2

        # Retropropagarea erorii
        delta_iesire = eroare * derivata_bipolara(iesire_finala)
        delta_ascuns = derivata_bipolara(iesire_ascuns[:-1]) * np.dot(greutati_ascuns_iesire[:-1], delta_iesire)

        # Actualizam greutatile
        greutati_ascuns_iesire += rata_instruire * np.outer(iesire_ascuns, delta_iesire)
        greutati_intrare_ascuns += rata_instruire * np.outer(intrare, delta_ascuns)

    # Verificam daca eroarea este suficient de mica
    eroare_totala /= len(patternuri)
    if eroare_totala < eroare_tolerata:
        break

# Afisam rezultatele
print(f"Reteaua a fost antrenata in {epoca + 1} epoci cu eroarea finala {eroare_totala.item():.5f}\n")
print("Intrare          | Iesire dorita | Iesire calculata")
for i in range(len(patternuri)):
    intrare = patternuri[i]
    iesire_ascuns = activare_bipolara(np.dot(intrare, greutati_intrare_ascuns))
    iesire_ascuns = np.append(iesire_ascuns, 1)  # Bias
    iesire_finala = activare_bipolara(np.dot(iesire_ascuns, greutati_ascuns_iesire))
    print(f"{intrare[:-1] * 200}    | {iesiri_dorite[i]:6}        | {iesire_finala[0]:.5f}")
