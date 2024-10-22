import random
#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
aluno1=  input('nome do primeiro aluno: ')
aluno2= input('nome do segundo aluno: ')
aluno3= input('nome do terceiro aluno: ')
aluno4= input('nome do quarto aluno: ')
lista = aluno1,aluno2,aluno3,aluno4
sorteio= random.choice(lista)
print('o aluno sorteado foi o {}'.format(sorteio))