print('Calculo de 5% de comissão')

wage = float(input('Informe seu salário atual: '))

commission = wage * 5 / 100
atualwage = wage + commission

print(f'Sua comissão é de {commission:.2f} e somado, seu atual salário é de {atualwage:.2f}')