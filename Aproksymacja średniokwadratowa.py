import numpy as np
from numpy.linalg import inv

X = [int(x) for x in input("Podaj wartosci x: ").split()]
Y = [int(x) for x in input("Podaj wartosci y: ").split()]

if len(X) != len(Y):
    print("Liczby argumentow musza sie zgadzac")
    exit()

sizeRows = len(X)
sizeColumns = (int(input("Podaj stopien wielomianu przyblizajacego: ")) + 1)    # dla wielomianu 3-go stopnia

G = np.zeros((sizeRows, sizeColumns))

for i in range(sizeRows):
    for j in range(sizeColumns):
        G[i][j] = X[i]**(sizeColumns - j - 1)

GT = G.transpose()
d = np.reshape(Y, (sizeRows, 1))
GTd = GT @ d
GTG = np.matmul(GT, G)
invGTG = inv(GTG)
res = (invGTG @ GTd).ravel().tolist()

print(f"Wielomian przyblizajacy {sizeColumns -1}-go stopnia:")

for i in range(sizeColumns):
    print(f"{res[i]}", end="")
    if i != (sizeColumns - 1):
        print(f"x^{sizeColumns - i - 1} + ", end="")

