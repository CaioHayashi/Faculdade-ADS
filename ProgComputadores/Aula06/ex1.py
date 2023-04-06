import os
os.system('cls' if os.name == 'nt' else 'clear')

salario = float(input('Digite o salário fixo: '))
vendas = float(input('Digite o valor de vendas: '))

comissao = vendas * 0.04

print(f'Comissão: R${comissao:.2f}')
print(f'Salário final: R${salario + comissao:.2f}')