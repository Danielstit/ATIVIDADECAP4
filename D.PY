N1 = int(input("INFORME A PROMEIRA NOTA: "))
N2 = int(input("INFORME A SENGUNDA NOTA: "))
N3 = int(input("INFORME A TERCEIRA NOTA: "))
N4 = int(input("INFORME A QUARTA NOTA: "))

MD1=((N1+N2+N3+N4)/4)
if(MD1>=7):
    print(F'\nAPROVADO! || MEDIA = {MD1} PONTOS\n')
else:
    N5= int(input("INFORME A QUINTA NOTA: "))
    MD2 = ((MD1 + N5) / 2)
    if(MD2>=5):
        print(F"APROVADO EM EXAME! || MEDIA = {MD2}")
    else:
        print(F"REPROVADO!  || MÉDIA = {MD2}")
 