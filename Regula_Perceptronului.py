import csv
import numpy as np


def readfromcsv():
    myList = []
    file_path = 'C:/Users/PC/Desktop/iris.data'
    with open(file_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row) == 5 and row[4] != "Iris-virginica":
                myList.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
    return myList


def calculeaza_iesire(caracteristici, greutati):
    activare = np.dot(caracteristici, greutati)
    return 1 if activare >= 0 else -1


def ajusteaza_greutati(caracteristici, greutati, rata_invatare, eticheta_corecta):
    iesire = calculeaza_iesire(caracteristici, greutati)
    if iesire != eticheta_corecta:
        modificare = 2 * rata_invatare * np.array(caracteristici) * (eticheta_corecta - iesire)
        greutati += modificare
        return greutati, 1
    return greutati, 0

if __name__ == '__main__':
    
    set_date = readfromcsv()
    if not set_date:
        print("Eroare: Nu s-au găsit date.")
        exit()

    greutati_initiale = np.array([1, -1, 0, 0.5])
    date_setosa = set_date[:5]
    date_versicolor = set_date[-5:]
    date_antrenament = date_setosa + date_versicolor

    rata_invatare = 0.01
    numar_maxim_epoci = 100
    epoca_curenta = 0
    numar_greseli = 1
    greutati = greutati_initiale

   
    while epoca_curenta < numar_maxim_epoci and numar_greseli > 0:
        numar_greseli = 0
        for index, punct in enumerate(date_antrenament):
            eticheta_corecta = 1 if index < len(date_setosa) else -1
            greutati, eroare = ajusteaza_greutati(punct, greutati, rata_invatare, eticheta_corecta)
            numar_greseli += eroare

        print(f"Epoca {epoca_curenta}: {numar_greseli} clasificări greșite")
        epoca_curenta += 1

    print(f"Greutăți finale: {greutati}")

   
    greseli_totale = 0
    for index, punct in enumerate(set_date):
        eticheta_corecta = 1 if index < len(set_date) // 2 else -1
        iesire_obtinuta = calculeaza_iesire(punct, greutati)
        if iesire_obtinuta != eticheta_corecta:
            greseli_totale += 1

    rata_eroare = round((greseli_totale / len(set_date)) * 100, 2)
    print(f"Rată de eroare: {rata_eroare}%")
