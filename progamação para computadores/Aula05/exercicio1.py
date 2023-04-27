import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Classe Eleitoral')
idade = int(input('Digite sua idade: '))

if idade < 16:
    print('não-eleitor')
elif idade >= 18 and idade <= 65:
    print('eleitor obrigatório')
else:
    print('eleitor facultativo')