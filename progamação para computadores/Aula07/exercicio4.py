import os
os.system('cls' if os.name == 'nt' else 'clear')

negativos = 0
positivos = 0
menorNum = 0
for i in range(10):
    num = float(input('Digite um número: '))

    if num >= 0:
        positivos += 1
    else:
        negativos += 1
        
    if menorNum == 0:
        menorNum = num
    elif menorNum > num:
        menorNum = num

print(f'positivos: {positivos}')
print(f'negativos: {negativos}')
print(f'menor número: {menorNum}')