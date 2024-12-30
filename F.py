A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
AUX=0

if(A>B):
    A,B=B,A
if(A>C):
    A,C=C,A
if(B>C):
    B ,C = C, B

print(F'\n ORDEM CRESCENTE: {A} {B} {C}\n')