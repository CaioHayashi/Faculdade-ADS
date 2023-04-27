import os
os.system('cls' if os.name == 'nt' else 'clear')

nota1 = float(input('Digite a primeira nota parcial: '))
nota2 = float(input('Digite a segunda nota parcial: '))

media = ( nota1 + nota2 ) / 2
print(f'Média: {media}')

if media <= 10 and media >= 6:
    if media >= 9:
        print('Conceito: A')
    elif media >= 7.5:
        print('Conceito: B')
    else:
        print('Conceito: C')
    print('APROVADO')

elif media < 6 and media >= 0:
    if media >= 4:
        print('Conceito: D')
    else:
        print('Conceito: E')
    print('REPROVADO')

else:
    print('Nota informada incorreta')