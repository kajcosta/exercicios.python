#crie um algoritmo que mostre seu dobro seu triplo e sua raiz quadrada
n = int(input('escreva um número: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)
print('Você digitou {}, o dobro desse numero é {}, '.format(n, dobro),end='')
print('o triplo é {} e a raiz quadradada é {}'.format(triplo, raiz))