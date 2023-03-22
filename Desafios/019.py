# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que o ajude, lendo o nome dos alunos e escrevendo o nome do escolhido de forma aleatória(random).
from random import choice
nome01 = str(input('Primeiro aluno(a): '))
nome02 = str(input('Segundo aluno(a): '))
nome03 = str(input('Terceiro aluno(a): '))
nome04 = str(input('Quarto aluno(a): '))
lista = [nome01, nome02, nome03, nome04]
escolhido = choice(lista)
print('O aluno(a) escolhido(a) foi {},parabéns!'.format(escolhido))
