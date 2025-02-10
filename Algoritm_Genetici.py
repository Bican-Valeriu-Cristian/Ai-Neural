import random
import numpy as np

def genereaza_populatie(marime, gene):
    return [np.random.randint(0, 2, gene).tolist() for _ in range(marime)]

def calcul_performanta(cromozom):
    pachet1 = [i + 1 for i, gena in enumerate(cromozom) if gena == 0]
    pachet2 = [i + 1 for i, gena in enumerate(cromozom) if gena == 1]
    return 1 / (1 + abs(36 - sum(pachet1)) + abs(360 - (np.prod(pachet2) if pachet2 else 0)))

def selectie(populatie, performante):
    return random.choices(populatie, weights=[p / sum(performante) for p in performante], k=2)

def incrucisare(parinte1, parinte2):
    punct = random.randint(1, len(parinte1) - 1)
    return parinte1[:punct] + parinte2[punct:], parinte2[:punct] + parinte1[punct:]

def mutatie(cromozom, rata):
    return [gena if random.random() > rata else 1 - gena for gena in cromozom]

def algoritm_genetic(generatii, marime_populatie, gene, rata_mutatie):
    populatie = genereaza_populatie(marime_populatie, gene)
    for _ in range(generatii):
        performante = [calcul_performanta(c) for c in populatie]
        populatie_urmatoare = []
        while len(populatie_urmatoare) < marime_populatie:
            parinte1, parinte2 = selectie(populatie, performante)
            copil1, copil2 = incrucisare(parinte1, parinte2)
            populatie_urmatoare += [mutatie(copil1, rata_mutatie), mutatie(copil2, rata_mutatie)]
        populatie = populatie_urmatoare[:marime_populatie]
    performante = [calcul_performanta(c) for c in populatie]
    cel_mai_bun = populatie[performante.index(max(performante))]
    pachet1 = [i + 1 for i, gena in enumerate(cel_mai_bun) if gena == 0]
    pachet2 = [i + 1 for i, gena in enumerate(cel_mai_bun) if gena == 1]
    return cel_mai_bun, pachet1, pachet2, sum(pachet1), np.prod(pachet2) if pachet2 else 0

solutie, pachet1, pachet2, suma_pachet1, produs_pachet2 = algoritm_genetic(100, 50, 10, 0.1)
print("Solutie binara:", solutie)
print("Pachet 1 (suma cât mai aproape de 36):", pachet1, "Suma:", suma_pachet1)
print("Pachet 2 (produs cât mai aproape de 360):", pachet2, "Produs:", produs_pachet2)