NOME = str(input("\nINFORME O NOME: \n"))
SEXO = str(input('\nINFORME O SEXO:\n[S]PARA FEMININO\n[M]PARA MASCULINO\n'))

if SEXO == "M" or SEXO == "F":
    if SEXO == 'M':
        print(F'Ilmo. Sr. {NOME}')
    elif SEXO == 'F':
        print(F'Ilmo. Sr. {NOME}')
else:
    print(F'SEXO INVALIDO')