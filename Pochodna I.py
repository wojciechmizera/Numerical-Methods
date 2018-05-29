

h = 0.1

fx = input("Podaj funkcje: ")
x = int(input("Podaj x: "))

fx = fx.replace("^", "**")

fxminus2 = fx.replace("x", "(x - 2 * h)")
fxminus1 = fx.replace("x", "(x - 1 * h)")
fxplus1 = fx.replace("x", "(x + 1 * h)")
fxplus2 = fx.replace("x", "(x + 2 * h)")


expression = f"(1/(12 * h))*( ({fxminus2}) - 8 * ({fxminus1}) + 8 * ({fxplus1}) - ({fxplus2}) )"

print("Pochodna w punkcie wynosi:")

print(eval(expression))
