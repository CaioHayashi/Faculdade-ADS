binario = input('Digite um número binário: ')
n = len(binario)-1
decimal = 0

for d in binario:
    decimal += int(d) * 2 ** n
    n = n - 1

print(f'{binario}(2) = {decimal}(10)')