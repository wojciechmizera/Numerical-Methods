

h = 0.1

fx = input("Podaj funkcje: ")
x = int(input("Podaj x: "))

fx = fx.replace("^", "**")

fxminus2 = fx.replace("x", "(x - 2 * h)")
fxminus1 = fx.replace("x", "(x - 1 * h)")
fxplus1 = fx.replace("x", "(x + 1 * h)")
fxplus2 = fx.replace("x", "(x + 2 * h)")


expression = f"(1/(3 * h ** 2))*( ({fxminus2}) - ({fxminus1}) - ({fxplus1}) + ({fxplus2}) )"

print("Druga Pochodna w punkcie wynosi:")

print(eval(expression))
