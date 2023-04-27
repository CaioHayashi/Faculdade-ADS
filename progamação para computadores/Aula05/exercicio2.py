import os, math
os.system('cls' if os.name == 'nt' else 'clear')

print('Equação de segundo grau')
print('Informe os coeficientes:')
a = int(input('Coeficiente A: '))
b = int(input('Coeficiente B: '))
c = int(input('Coeficiente C: '))

if a == 0:
    print("Não é equação do segundo grau")
else:
    delta = b**2 - 4 * a * c

    if delta >= 0:
        raiz1 = (-(b) + (math.sqrt(delta))) / 2
        raiz2 = (-(b) - (math.sqrt(delta))) / 2

        print(f'o resultado é primeira raiz igual a {raiz1}, e a segunda igual a {raiz2}.')
    else:
        print('Não há raízes reais')
