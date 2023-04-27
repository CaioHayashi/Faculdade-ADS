conta = input('Digite o número da conta com 4 algarismo: ')
soma = 0

for i in conta:
    soma += int(i)

digito = soma % 10

print(f'00{conta}-{digito}')
