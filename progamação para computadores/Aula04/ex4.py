import os
os.system('cls' if os.name == 'nt' else 'clear')

agua = float(input('Digite o valor da sua conta de água: '))
luz = float(input('Digite o valor da sua conta de luz: '))
telefone = float(input('Digite o valor da sua conta de telefone: '))

salario = float(input('Digite o valor do seu salário atual: '))

totalContas = agua + luz + telefone

if salario >= totalContas:
    restoSalario = salario - totalContas
    print(f'Após pagar suas contas, restará {restoSalario}')
else:
    print('Valor insuficiente!')