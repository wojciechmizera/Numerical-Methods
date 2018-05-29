X = [float(x) for x in input("Podaj wartosci x: ").split()]

Y = [float(y) for y in input("Podaj wartosci y: ").split()]

if X.__len__() != Y.__len__():
    print("The number of elements in both tables should be the same")
    exit()

inputX = [float(y) for y in input("Podaj szukane x: ").split()]
outputY = []

for s in range(len(inputX)):
    outputY.append(0)
    for i in range(len(X)):
        licznik = 1
        mianownik = 1
        for k in range(len(X)):
            if k != i:
                licznik = licznik * (inputX[s] - X[k])
                mianownik = mianownik * (X[i] - X[k])
        outputY[s] = outputY[s] + (licznik/mianownik) * Y[i]
    print("f(", inputX[s], ") = ", outputY[s])
