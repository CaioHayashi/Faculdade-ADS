import os
os.system('cls' if os.name == 'nt' else 'clear')

str = input("Digite uma string: ").upper()


for letra in set(str):
    contador = str.count(letra)
    print(f'O caractere {letra} aparece {contador} vezes na string.')
        
