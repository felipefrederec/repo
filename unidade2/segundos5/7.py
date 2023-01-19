#7.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


repetir = 1
while repetir == 1:
    nome = str(input('informe o nome de usuario: '))
    senha = str(input('informe a senha: '))
    if nome==senha:
        print ('ERRO: a senha nao pode ser igual ao nome de usuario')
    else:
        repetir = 0
        print ('os dados cadastrados foram:')
        print ('nome de usuario: ', nome)
        print ('senha: ', senha)

