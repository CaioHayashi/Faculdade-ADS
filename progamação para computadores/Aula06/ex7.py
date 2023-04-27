import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Coordernadas de um ponto P(x, y)')

x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordernada y: '))

if x > 0 and y > 0:
    print(f'O ponto P({x}, {y}) pertence ao 1º quadrante')
elif x < 0 and y > 0:
    print(f'O ponto P({x}, {y}) pertence ao 2º quadrante')
if x < 0 and y < 0:
    print(f'O ponto P({x}, {y}) pertence ao 3º quadrante')
if x > 0 and y < 0:
    print(f'O ponto P({x}, {y}) pertence ao 4º quadrante')
