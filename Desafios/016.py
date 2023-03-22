# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex 6.98765
from math import trunc
num = float(input('Digite um número!:'))
print('O número {} tem a parte inteira de {}'.format(num, trunc(num)))

# print('O valor digitado foi {} e sua porção inteira é {}'.format(num,trunc(num)))
# print ('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
