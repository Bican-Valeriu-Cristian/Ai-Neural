import numpy as np

pettern = np.array([[45, 85],
                    [50, 43],
                    [40, 80],
                    [55, 42],
                    [200, 43],
                    [48, 40],
                    [195, 41],
                    [43, 87],
                    [190, 40]])

nr_epoci = 10  
c = 0.1

np.random.seed(0) 
w1 = np.random.rand(2) * 100
w2 = np.random.rand(2) * 100
w3 = np.random.rand(2) * 100

pct_random = np.array([w1, w2, w3])

def dist_pct(p1, p2):
    return np.linalg.norm(p1 - p2)

for epoci in range(nr_epoci):
    print(f"\nEpoca {epoci + 1}")
    for i, x in enumerate(pettern):
        
        distanta = [dist_pct(x, w) for w in pct_random]
        contor_win = np.argmin(distanta) 
        print(f"Pattern {i + 1}: {x}, Prototip câștigător: w{contor_win + 1 }")
        
        pct_random[contor_win] = pct_random[contor_win] + c * (x - pct_random[contor_win]) #actualizare lista ? 

print("\nPrototipuri finale după instruire:")
for i, w in enumerate(pct_random):
    print(f"w{i + 1}: {w}")