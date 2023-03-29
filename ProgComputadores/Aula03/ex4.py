import os
os.system('cls')

valorPrestacao = float(input('Digite o valor da prestação: '))
multa = float(input('Digite a porcentagem da multa: '))
qtdeDias = int(input('Digite a quantidade de dias em atraso: '))


prestação = valorPrestacao + (valorPrestacao * (multa/100) * qtdeDias)

print(f'O valor da prestação é R${prestação:.2f}')