import csv
def readfromcsv():
    myList = []
    file_path = 'C:/Users/PC/Desktop/Salary_Data.csv'
    with open(file_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)  
        for row in readCSV:
            if len(row) >= 2:
                try:
                    myList.append([float(row[0]), float(row[1])])
                except ValueError:
                    print(f"Valoare invalidă la linia: {row}")
    return myList

def linear_regression(data, c=0.01, epochs=1000):
    n = len(data)
    w1, w2 = 0.0, 0.0  
    
    for epoch in range(epochs):
        
        gradient_w1 = -1 / n * sum((data[i][1] - (w1 * data[i][0] + w2)) * data[i][0] for i in range(n))
        gradient_w2 = -1 / n * sum((data[i][1] - (w1 * data[i][0] + w2)) for i in range(n))
        
        
        w1 = w1 - c * gradient_w1
        w2 = w2 - c * gradient_w2
        
        
        if epoch % 100 == 0:
            error = sum((data[i][1] - (w1 * data[i][0] + w2))**2 for i in range(n)) / (2 * n)
            print(f"Epoca {epoch}: Eroare = {error:.6f}, w1 = {w1:.4f}, w2 = {w2:.4f}")
    
    print(f"\nCoeficienții finali: w1 = {w1:.4f}, w2 = {w2:.4f}")
    return w1, w2


data = readfromcsv()
w1, w2 = linear_regression(data, c=0.01, epochs=5000)
print(f"\nLinia de regresie obținută: y = {w1:.4f} * x + {w2:.4f}")