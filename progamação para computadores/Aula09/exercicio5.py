import os
os.system('cls' if os.name == 'nt' else 'clear')

res = "Fizz Buzz"
palavras = res.split()
num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0: 
    print(palavras[0], palavras[1])
elif num % 3 == 0:
    print(palavras[0])
elif num % 5 == 0:
    print(palavras[1])
else:
    print(num)
