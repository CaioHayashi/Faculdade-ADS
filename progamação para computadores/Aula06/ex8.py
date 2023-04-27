import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input('Qual o seu nome: ')
horas = int(input('Que horas são [0-23]?'))

if horas >= 0 and horas <= 23:
    if horas >= 5 and horas <= 12:
        saudacao = 'Bom dia'
    elif horas > 12 and horas <= 18:
        saudacao = 'Boa tarde'
    else:
        saudacao = 'Boa noite'
else:
    print('hora incorreta')

print(f'{saudacao} {nome}')