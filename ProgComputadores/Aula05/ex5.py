import os
os.system('cls' if os.name == 'nt' else 'clear')

valorCompra = int(input('Digite o valor da compra: '))
parcela = int(input('Digite o número de parcelas: '))


""" if parcela == 2:
    print(f'x{parcela} de R${(valorCompra / parcela) * 0.03:.2f}')
elif parcela == 4:
    print(f'x{parcela} de R${(valorCompra / parcela) * 0.07:.2f}')
elif parcela == 8:
    print(f'x{parcela} de R${(valorCompra / parcela) * 0.09:.2f}')
elif parcela == 12:
    print(f'x{parcela} de R${(valorCompra / parcela) * 0.12:.2f}')
else:
    print('Número de parcelas inválido') """

match (parcela):
    case 2:
        valorCompra = valorCompra * 1.03
    case 4:
        valorCompra = valorCompra * 1.07
    case 6:
        valorCompra = valorCompra * 1.09
    case 8:
        valorCompra = valorCompra * 1.12
    case _:
        valorCompra = 0