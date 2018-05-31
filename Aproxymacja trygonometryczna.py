import numpy as np


X = [float(x) for x in input("Podaj wartosci x: ").split()]
Y = [float(y) for y in input("Podaj wartosci y: ").split()]
x0 = [float(x0) for x0 in input("Podaj szukane wartosci x:").split()]

# X = [np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi]
# Y = [3, 4, 1, 0]
# x0 = [5, 6, 7]

if len(X) != len(Y):
    print("Liczba argumentow musi byc rowna liczbe wartosci")
    exit()

N = len(X)
m = int((N - 1) / 2)

a0 = (1 / N) * sum(Y)

a = []
b = []

for k in range(1, m + 1):
    valueA = 0
    valueB = 0
    for i in range(1, N+1):
        valueA += Y[i - 1] * np.cos((2 * np.pi) / N * k * i)
        valueB += Y[i - 1] * np.sin((2 * np.pi) / N * k * i)
    a.append(valueA * 2 / N)
    b.append(valueB * 2 / N)

fx = np.empty(len(x0))
fx.fill(float(a0))

for x in range(len(x0)):
    for i in range(0, m):
        fx[x] += a[i] * np.cos(x0[x] * (i+1)) + b[i] * np.sin((x0[x] * (i+1)))
    print(f"x = {x0[x]}\ty = {fx[x]}")
