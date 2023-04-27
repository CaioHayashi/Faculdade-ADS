import os
os.system('cls' if os.name == 'nt' else 'clear')

resp = 's'
cont = 0
soma = 0

while resp in "sS":
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    resp = input('Deseja continuar (s/n)? ')

media = soma / cont

print(f'A média dos números digitados é: {media:.2f}')