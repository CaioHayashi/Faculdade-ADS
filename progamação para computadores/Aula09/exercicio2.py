import os
os.system('cls' if os.name == 'nt' else 'clear')

num = input("Digite um número com três algarismos: ")
numReverse = num[::-1]
soma = int(num) + int(numReverse)

print(f'O inverso do número é: {numReverse}')
print(f'A soma é {num} + {numReverse} = {soma}')