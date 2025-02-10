import numpy as np

date_intrare = [[45, 85, -1], [50, 43, -1], [40, 80, -1], [55, 42, -1],
                [200, 43, -1], [48, 40, -1], [195, 41, -1], [43, 87, -1], [190, 40, -1]]
iesiri_dorite = np.array([[1, -1, -1], [-1, 1, -1], [1, -1, -1], [-1, 1, -1],
                          [-1, -1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1], [-1, -1, 1]])

minime = np.min(date_intrare, axis=0)[:-1]
maxime = np.max(date_intrare, axis=0)[:-1]
date_normalizate = []

for date in date_intrare:
    scalate = [(valoare - minime[i]) / (maxime[i] - minime[i]) for i, valoare in enumerate(date[:-1])]
    scalate.append(-1)
    date_normalizate.append(scalate)

date_normalizate = np.array(date_normalizate)
greutati = 2 * np.random.random((3, 3)) - 1
rata_aprendere = 0.1
eroare_limita = 0.0005
max_iteratii = 10000
iteratie = 0

def functie_activare(net):
    return (2 / (1 + np.exp(-net))) - 1

while True:
    iesiri = []
    for i in range(len(date_normalizate)):
        iesiri.append(functie_activare(np.dot(greutati, date_normalizate[i])))
    iesiri = np.array(iesiri)

    for p in range(len(date_normalizate)):
        for j in range(len(iesiri[0])):
            for i in range(len(date_normalizate[0])):
                greutati[j, i] += rata_aprendere * (iesiri_dorite[p, j] - iesiri[p][j]) * (1 - iesiri[p][j] ** 2) * date_normalizate[p, i]

    eroare = np.sum((iesiri_dorite - iesiri) ** 2) / len(iesiri_dorite)
    iteratie += 1
    if eroare < eroare_limita or iteratie >= max_iteratii:
        break

iesiri_finale = []
for i in range(len(date_normalizate)):
    iesiri_finale.append(functie_activare(np.dot(greutati, date_normalizate[i])))

for i, iesire in enumerate(iesiri_finale):
    print(f"Date: {date_intrare[i]} -> Dorite: {iesiri_dorite[i]} -> Predicție: {iesire}")
