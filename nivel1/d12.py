#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto=float(input('preço do produto: ')) 
desconto= produto*(5/100)
print('o novo preço será: {:.2f}'.format(desconto))