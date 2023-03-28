import os, math
os.system('cls')

h = float(input('Informe a altura do tronco da pirâmide: '))
bMenor = float(input('Informe a a base menor: '))
bMaior = float(input('Informe a base maior: '))

volume = h / 3 * (
    math.pow(bMaior, 2) + math.pow(bMenor, 2) +
    math.sqrt((math.pow(bMaior, 2) * math.pow(bMenor, 2))) 
)

print(f'{volume:.2f}')