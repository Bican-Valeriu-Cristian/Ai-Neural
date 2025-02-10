# Algoritmi de Inteligenta Artificiala - Retele Neuronale

Acest proiect explorează diferiți algoritmi de învățare automată și rețele neuronale, implementați în Python. Algoritmii acoperă diverse tehnici precum regresia liniară, regula delta, clustering K-means, perceptron, regula Hebb, algoritmul de propagare înapoi a erorii, algoritmul "câștigătorul ia tot" și algoritmi genetici.

## Descriere

Acest proiect implementează diferite reguli și algoritmi pentru antrenarea rețelelor neuronale, fiecare având aplicabilități specifice în probleme de clasificare, regresie și optimizare. Algoritmii sunt scriși în Python și folosesc biblioteci precum NumPy, TensorFlow și scikit-learn.

## Algoritmi Implementați

### 1. **Regresie Liniară**
   - Model matematic pentru a estima o relație liniară între variabile.
   - Folosește metoda celor mai mici pătrate pentru ajustarea coeficienților.

### 2. **Regula Delta**
   - Tehnică de antrenare a unui neuron artificial.
   - Se bazează pe actualizarea ponderilor folosind diferența dintre valoarea dorită și cea prezisă.

### 3. **K-Means Clustering**
   - Algoritm de învățare nesupravegheată pentru gruparea datelor.
   - Folosește distanța Euclidiană pentru a atribui punctele de date unui grup (cluster).

### 4. **Regula Perceptronului**
   - Algoritm de clasificare liniară bazat pe ajustarea ponderilor în funcție de erori.
   - Funcționează bine pentru date separabile liniar.

### 5. **Regula Hebb**
   - Principiu de învățare neuronală bazat pe întărirea conexiunilor sinaptice în funcție de activitatea neuronilor.
   - Folosit pentru modelarea memoriei asociative.

### 6. **Algoritmul Backpropagation of Error**
   - Algoritm folosit în rețele neuronale multi-strat (MLP).
   - Utilizează propagarea inversă a erorii pentru ajustarea ponderilor în cadrul rețelei.

### 7. **Algoritmul "Câștigătorul ia tot" (Winner-Takes-All)**
   - Model competitiv de învățare în care neuronii concurează pentru activare.
   - Aplicat în rețelele Kohonen și auto-organizare.

### 8. **Algoritmi Genetici**
   - Algoritmi de optimizare inspirați din selecția naturală.
   - Utilizează operații precum selecția, crossover-ul și mutația pentru a îmbunătăți soluțiile candidate.

## Cerinte

- Python 3.8+
- Biblioteci necesare:
  ```bash
  pip install numpy pandas matplotlib scikit-learn tensorflow
  ```

## Structura Proiectului

| Fișier/Folder | Descriere |
|--------------|-----------|
| `Regresie_Liniara.py` | Implementare a regresiei liniare |
| `Regula_Delta.py` | Implementare a regulii delta |
| `Regula_K-means_clustering.py` | Implementare a algoritmului K-Means |
| `Regula_Perceptronului.py` | Implementare a regulii perceptronului |
| `RegulaHebb.py` | Implementare a regulii Hebb |
| `Algoritm_Backpropagation_of_error.py` | Implementare a algoritmului Backpropagation |
| `Algoritm_câștigătorul_ia_tot.py` | Implementare a algoritmului Winner-Takes-All |
| `Algoritm_Genetici.py` | Implementare a algoritmilor genetici |
| `README.md` | Acest fișier |
| `LICENSE` | Licența proiectului |


## Licență

Acest proiect este distribuit sub licența MIT. Vezi fișierul `LICENSE` pentru mai multe detalii.

