preco_normal = float(input('Qual o preço do produto? R$ '))
preco_descontado = preco_normal - (preco_normal * 5/100)
print('O novo preço com desconto de 5% é de R$ {:.2f}'.format(
    preco_descontado))
