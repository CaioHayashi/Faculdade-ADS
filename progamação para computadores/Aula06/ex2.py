import os
os.system('cls' if os.name == 'nt' else 'clear')

segundos = int(input('Digite a quantade de segundos: '))

horas = segundos // 3600
minutos = segundos % 3600 // 60
segundos = segundos % 60

print(f'{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)')