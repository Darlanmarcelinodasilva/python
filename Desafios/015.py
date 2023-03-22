# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado , a quantidade de dias pelos quais foi algugado.Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.
dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quilometragem percorrida? '))
total = (dias * 60) + (km * 0.15)
print('Você alugou o carro por {} dias ,\npercorreu {}Km , \ne terá que pagar R${:.2f}'.format(dias, km, total))
