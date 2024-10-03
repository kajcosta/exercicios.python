 #escreva um programa que leia um valor em metros e exiba a conversão em centímetros e milimetros
m=int(input('medida em metros: '))
cm=m*100
mm=m*1000
print('{} metros é equivalente a {} centímetros e também a {} milímetros.'.format(m, cm, mm))
