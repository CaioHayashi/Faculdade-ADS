import os
os.system('cls')

value = float(input('Digite o valor gasto no restaurante ComaBem: '))

comission = (value * 10) / 100

total = comission + value

print(f'O valor total da conta foi R${total:.2f}, sendo R${comission:.2f} equivalente a 10% do garçom.')