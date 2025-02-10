import numpy as np

puncte = np.array([
    [45, 85],
    [50, 43],
    [40, 80],
    [55, 42],
    [200, 43],
    [48, 40],
    [195, 41],
    [43, 87],
    [190, 40]
])


numar_clustere = 3
numar_maxim_iteratii = 100


np.random.seed(42)
centroizi = puncte[np.random.choice(len(puncte), numar_clustere, replace=False)]


def distanta_euclideana(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


for iteratie in range(numar_maxim_iteratii):
    
    clustere = [[] for _ in range(numar_clustere)]
    for i in range(len(puncte)):
        punct = puncte[i]
        distante = [distanta_euclideana(punct, centroid) for centroid in centroizi]

        
        distanta_minima = distante[0]
        index_cluster = 0
        for j in range(1, len(distante)):
            if distante[j] < distanta_minima:
                distanta_minima = distante[j]
                index_cluster = j

       
        clustere[index_cluster] += [i]  

 
    noi_centroizi = np.zeros_like(centroizi)
    for k in range(numar_clustere):
        if len(clustere[k]) > 0:
            suma = np.zeros_like(puncte[0])
            for idx in clustere[k]:
                suma += puncte[idx]
            noi_centroizi[k] = suma / len(clustere[k])
        else:
            noi_centroizi[k] = centroizi[k]  

   
    if np.allclose(centroizi, noi_centroizi):
        break

    centroizi = noi_centroizi


print("Centroizi finali:")
for i in range(numar_clustere):
    print(f"Cluster {i + 1}: {centroizi[i]}")

print("\nPuncte asociate fiecărui cluster:")
for i in range(numar_clustere):
    puncte_cluster = [puncte[idx].tolist() for idx in clustere[i]]
    print(f"Cluster {i + 1}: {puncte_cluster}")
