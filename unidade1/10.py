#10.Faça um Programa que leia três números e mostre o maior deles.

numero1 = int(input('informe um numero '))
numero2 = int(input('informe outro numero '))
numero3 = int(input('informe mais um numero '))

maior = numero1

if numero2>=maior: 
	maior=numero2
if numero3>=maior:
    maior=numero3

print('o maior numero é', maior)

