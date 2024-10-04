#faça um programa que leia a altura e largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m^2
altura=float(input('altura em metros da parede: '))
largura= float(input('largura em metros da parede: '))
mquadrados= altura*largura
tinta=mquadrados/2
print('a parede tem {:.1f} em metros quadrados e precisa de {:.1f}  litros de tinta para pintala toda'.format(mquadrados,tinta))