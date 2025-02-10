import numpy as np

#Ex 1
x1 = np.array([[1], [-2], [1.5], [0]])
x2 = np.array([[1], [-0.5], [-2], [-1.5]])
x3 = np.array([[0], [1], [-1], [1.5]])

X = [x1, x2, x3]

w = np.array([[1], [-1], [0.5], [0]])

def bipolar(exemplu):
    return np.sign(exemplu)

def bipolar_continuu(exemplu, lambda_=1):
   return (2 / (1 + np.exp(-lambda_ * exemplu))) - 1

for x in X:
    exemplu = np.dot(w.T, x) 
    y = bipolar(exemplu)
    w = w + x * y
    print(" bipolară:\n", w)


# x1 = np.array([[1], [-2]])
# x2 = np.array([[0], [1]])
# x3 = np.array([[2], [3]])
# x4 = np.array([[1], [-1]])

# X = [x1, x2, x3, x4]

# w = np.array([[1], [-1]])

# def bipolar_binar(exemplu):
#     return np.sign(exemplu)

# def bipolar_continuu(exemplu, lambda_=1):
#     return (2 / (1 + np.exp(-lambda_ * exemplu))) - 1


# w = np.array([[1], [-1]]) 
# print("Ponderi inițiale bipolară binară:\n", w)

# for x in X:
#     exemplu = np.dot(w.T, x)
#     y = bipolar_binar(exemplu)
#     w = w + x * y
#     print("Pondere bipolară binară:\n", w)


# w = np.array([[1], [-1]])  
# print("\nPonderi inițiale bipolară continuă:\n", w)

# for x in X:
#     exemplu = np.dot(w.T, x)
#     y = bipolar_continuu(exemplu)
#     w = w + x * y
#     print("Pondere bipolară continuă:\n", w)

