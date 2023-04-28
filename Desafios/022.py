nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('O seu nome em MAIÚSCULAS é {}'.format(nome.upper()))
print('O seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
# ou print ('O seu primeiro nome tem ao todo {} letras'.format(nome.find(' '))

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# => O nome de todo com letras maiúsculas
# => O nome de todo em minúsculas
# => Quantas letras ao todo (sem considerar espaços)
# => Quantas letras tem o primeiro nome