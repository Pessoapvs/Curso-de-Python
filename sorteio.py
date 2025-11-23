import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceeiro aluno: '))
n4 = str(input('Digite ó nome do quarto aluno: '))
lista=[n1, n2, n3, n4]
escolhido=random.choice(lista)
print('O Escolhodo e: {}'.format(escolhido))