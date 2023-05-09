import os
os.system('cls' if os.name == 'nt' else 'clear')

str = input('Digite uma palavra: ')

if str == str[::-1]:
    print(f'A palavra "{str}" é um palíndromo')
else:
    print(f'A palavra "{str}" não é palíndromo')