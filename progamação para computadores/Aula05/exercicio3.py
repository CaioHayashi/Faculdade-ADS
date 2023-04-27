import os
os.system('cls' if os.name == 'nt' else 'clear')

produto = input('Digite o nome do produto: ')
valorCompra = float(input('Digite o valor da compra: '))

if valorCompra < 10:
    porcent = .7
elif valorCompra >= 10 and valorCompra < 30:
    porcent = .5
elif valorCompra >= 30 and valorCompra < 50:
    porcent = .4
elif valorCompra >= 50:
    porcent = .3

lucro = valorCompra * porcent
valorVenda = valorCompra + lucro

print(f'Produto: {produto}')
print(f'Valor de venda: {valorVenda}')