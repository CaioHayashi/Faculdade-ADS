valorHora = float(input('Digite o valor da hora aula: '))
horaSemanal = int(input('Digite a carga horária semanal: '))

salariaBase = valorHora * horaSemanal * 4.5
adicional = salariaBase * 1 / 6
salarioFinal = salariaBase + adicional

print(f'Salário final R${salarioFinal:.2f}')
