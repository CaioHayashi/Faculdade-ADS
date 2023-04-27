#num % 2 
#num // 2

num = int(input('Digite um número decimal: '))

binario = ''

while num > 0:
    r = num % 2

    if r == 10: r = 'A'

    binario += str(num % 2)
    num = num  // 2

print(binario)