import os
os.system('cls' if os.name == 'nt' else 'clear')
from random import *
numRandom = randint(0, 100)
print(numRandom)

print('Adivinhe meu número:')


while True:
    num = int(input('Digite um número entre 0 - 100: '))
    if num > numRandom:
        print('Digite um número menor')
    elif num < numRandom:
        print('Digite um número maior')
    else:
        print('Você acertou!!!')
        break