media = float(input('Digite a media do aluno: '))
freq = float(input('Digite o percentual de presença'))

if freq < 75:
    print('Reprovado por faltas!')
elif media < 6:
    print('Reprovado por nota!!!')
else:
    print('Aprovado')