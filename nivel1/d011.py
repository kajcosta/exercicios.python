#faça um algoritmo que leia o salario de um funcionario e mostre o seu novo salario com 15% de aumento
salario=float(input('seu salario atual é de: '))
comAumento=salario+(salario*(15/100))
print('seu novo salario é  de {:.2f}'.format(comAumento))