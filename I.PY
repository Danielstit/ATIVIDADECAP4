
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
E = int(input("Digite o valor de E: "))


menor = maior = A


if B < menor:
    menor = B
if B > maior:
    maior = B

if C < menor:
    menor = C
if C > maior:
    maior = C

if D < menor:
    menor = D
if D > maior:
    maior = D

if E < menor:
    menor = E
if E > maior:
    maior = E


print(f"O menor valor informado é: {menor}")
print(f"O maior valor informado é: {maior}")
