real = float(input('Quantos( Reais você tem na carteira ? R$'))
dolar = real / 5.24
euro = real / 5.65
print('Você pode comprar US${:.2f} ou EUR{:.2f}'.format(dolar, euro))
