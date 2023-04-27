import os
os.system('cls' if os.name == 'nt' else 'clear')

turno = input('Digite o seu turno de trabalho, sendo "N" = norturno, e "M" para matutino: ')
horasTrabalhadas = int(input('Digite quantas horas foram trabalhadas: '))

if turno == 'M':
    print(f'{horasTrabalhadas * 37.50}')
elif turno == 'N':
    print(f'{horasTrabalhadas * 40}')
else:
    print('Valor informado incorreto. Digite o seu turno de trabalho, sendo "N" = norturno, e "M" para matutino')

