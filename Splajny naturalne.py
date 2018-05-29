import numpy as np

#X = [int(x) for x in input("Podaj kolejne wartosci x: ").split()]

X = [-1, 0, 1, 2, 3]

for i in range(1, len(X)):
    if X[i - 1] >= X[i]:
        print("Niewlasciwe dane wejsciowe")
        exit()

tanA = input("Podaj wartosc tg na poczatku wykresu [1]: ")
tanB = input("Podaj wartosc tg na koncu wykresu [0]: ")

# potrzebujemy obliczyc pochodna...

