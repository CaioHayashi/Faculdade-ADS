import os, math
os.system('cls' if os.name == 'nt' else 'clear')

area = float(input('Digite a área a ser pintada (em m²): '))

cobertura = area / 3
lata = math.ceil(cobertura / 18)
valorTotal = lata * 80

print(f'Você precisará comprar {lata} lata(s)')
print(f'O valor total a pagar será de R${valorTotal:.2f}')