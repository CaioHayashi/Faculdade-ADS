import os
os.system('cls' if os.name == 'nt' else 'clear')

altura = float(input('Digite a altura da pessoa em metros: '))
sexo = input('Digite o sexo da pessoa m/f: ')

if sexo in 'mM':
    masc = (72.7 * altura) - 58
    print(f'O peso ideal dessa pessa é {masc:.2f}')
elif sexo in 'fF':
    femi = (62.1 * altura) - 44.7
    print(f'O peso ideal dessa pessoa é {femi:.2f}')
else:
    print('sexo incorreto, use "m" ou "f"')