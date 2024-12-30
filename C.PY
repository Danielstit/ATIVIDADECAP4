N1 = int(input("INFORME A PROMEIRA NOTA: "))
N2 = int(input("INFORME A SENGUNDA NOTA: "))
N3 = int(input("INFORME A TERCEIRA NOTA: "))
N4 = int(input("INFORME A QUARTA NOTA: "))

MD=((N1+N2+N3+N4)/4)

if(MD>=5):
    print(F'\nAPROVADO! || MEDIA = {MD} PONTOS\n')
else:
    print(F"\nREPROVADO! || MEDIA = {MD}PONTOS\n")