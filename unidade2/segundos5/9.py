#6.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
repetir = 1
while repetir == 1:
    nota = int(input('informe uma nota de 0 a 10 '))
    if nota<0 or nota>10:
        print ('ERRO: valor invalida')
    else:
        repetir = 0
        print ('a nota que você informou foi', nota)

