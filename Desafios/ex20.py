# Sorteando uma ordem de apresentação de um trabalho.Faça um programa que leia o nome de 4 alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Primeiro aluno(a):'))
n2 = str(input('Segundo aluno(a):'))
n3 = str(input('Terceiro aluno(a):'))
n4 = str(input('Quarto aluno(a):'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
