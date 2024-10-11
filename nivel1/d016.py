import math
#crie um programa que leia o comprimento de um cateto oposto  e um cateto adjacente de um triangulo retangulo  e mostre o valor da hipotenusa
cttOposto= float(input('qual a medida do cateto oposto: '))
cttAdjacente= float(input('qual a mediida do cateto adjacente: '))
hipotenusa= math.sqrt(cttOposto**2 + cttAdjacente**2)
print('O valor da hipotenusa ê {:.2f}'.format(hipotenusa))
