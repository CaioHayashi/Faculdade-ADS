import os
os.system('cls' if os.name == 'nt' else 'clear')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('[1] Média')
print('[2] Diferença maior - menor')
print('[3] Produto')
print('[4] Divisão n1/n2')

opcao = int(input('Digite uma opção: '))

match (opcao):
    case 1:
        res = (num1 + num2) / 2
        print(f'Média = {res}')

    case 2:
        res = num1 - num2
        print(f'Diferença = {res}')

    case 3:
        res = num1 * num2
        print(f'Produto = {res}')

    case 4:
        if num1 == 0 or num2 == 0:
            print('Impossível dividir por zero!!!!')
        else:
            res = num1 / num2
            print(f'Divisão = {res}')

    case _:
        print('Opção inválida!')