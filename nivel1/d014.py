#: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('quantidade de km percorrida: '))
dias=int(input('quantidade de dias: '))
aPagar=(km*0.15)+ (dias*60)
print('você tera que pagar R${:.2f}'.format(aPagar))