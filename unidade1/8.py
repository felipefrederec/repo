#8.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('informe F para feminino e M para masculino '))
sexo = (sexo.upper())

if sexo=='M': 
    print('M - Masculino')
elif sexo=='F': 
    print('F - Feminino')
else:
    print('entrada invalida')