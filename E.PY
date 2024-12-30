import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))


if a != 0 and b != 0 and c != 0:

    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não há solução real")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Apenas uma solução real: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Duas soluções reais e diferentes: x1 = {x1}, x2 = {x2}")
else:
    print("A equação não é completa. Todos os coeficientes A, B e C devem ser diferentes de zero.")
