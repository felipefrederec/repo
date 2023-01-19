#9.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra'))
letraUpper = (letra.upper())

if letraUpper=='A' or letraUpper=='E' or letraUpper=='I' or letraUpper=='O' or letraUpper=='U' : 
    print('A letra ', letra,' é vogal')
else:
    print('A letra ', letra,' é consoante ou a entrada foi invalida')

