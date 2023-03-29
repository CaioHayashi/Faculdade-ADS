import os, math
os.system('cls')

year = float(input('Digite o ano que nasceu: '))
month = float(input('Digite o mês em que nasceu: '))
day = float(input('Digite o dia em que nasceu: '))

yearInDays = year * 365
monthInDays = month * 30

totalInDays = yearInDays + monthInDays + day


print(f'O total em dias é {totalInDays}')