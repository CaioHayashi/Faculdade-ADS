import os
os.system('cls' if os.name == 'nt' else 'clear')

valorCompra = float(input('Digite o valor da compra para possível desconto: '))

if valorCompra >= 200:
    desconto = valorCompra * 0.2
    valorComDesconto = valorCompra - desconto
    print(f'Valor da compra é de R${valorCompra:.2f}, e tendo 20% de desconto, fica: R${valorComDesconto:.2f}')
else:
    print(f'Valor abaixo de R$200.00, não há desconto, valor da compra: {valorCompra}')