import os
os.system('cls' if os.name == 'nt' else 'clear')

num = int(input('Digite um número inteiro: '))

if num > 0:
    print(f'O número {num} é positivo')
elif num < 0:
    print(f'O número {num} é negativo')
else:
    print('O número é nulo')