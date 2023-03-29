import os, math
os.system('cls')

grau = float(input('Digite um valor em graus: '))
rad = math.radians(grau)

cos = math.acos(rad)
sen = math.sin(rad)
tan = math.tan(rad)


print(f'Radiano = {rad:.3f}\nCosceno = {cos:.3f}\nSeno = {sen:.3f}\nTangente = {tan:.3f}')