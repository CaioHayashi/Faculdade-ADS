import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Calcule dois valores:')
valor1 = float(input('Digite o 1º valor: '))
valor2 = float(input('Digite o 2º valor: '))

operador = input('Digite qual operação deseja fazer [+, -, *, /]: ')

match(operador):
    case '+':
        res = valor1 + valor2
        print(f'A soma do {valor1} {operador} {valor2} é {res}')
    case '-':
        res = valor1 - valor2
        print(f'A soma do {valor1} {operador} {valor2} é {res}')
    case '*':
        res = valor1 * valor2
        print(f'A soma do {valor1} {operador} {valor2} é {res}')
    case '/':
        res = valor1 / valor2
        print(f'A soma do {valor1} {operador} {valor2} é {res}')
    case _:
        print('Operador inválido!')