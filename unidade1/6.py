#6.Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('informe um numero '))
numero2 = int(input('informe outro numero '))

maior = numero1

if numero2>numero1: 
	maior=numero2

print('o maior numero é', maior)
