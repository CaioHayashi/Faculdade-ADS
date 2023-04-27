import os
os.system('cls' if os.name == 'nt' else 'clear')

soma = 0
num = int(input('Digite um número inteiro e positivo: '))

for i in range(1, num):
    soma += (1 / i)
    print(soma)

print(soma)