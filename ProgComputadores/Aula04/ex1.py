import os
os.system('cls' if os.name == 'nt' else 'clear')

num = int(input('Digite um número entre 0 a 9: '))

if num > 0 and num < 9:
    print('valor correto')
else: 
    print('valor incorreto')

