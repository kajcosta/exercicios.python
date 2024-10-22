import math
# faça um programa que leia um angulo qualquer e mostre o valor do seno, cosseno e tangente
angulo= float(input('qual o angulo: '))
rangulo = math.radians(angulo)
seno = math.sin(rangulo)
coss =math.cos(rangulo)
tang =math.tan(rangulo)
print ('o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, coss, tang))