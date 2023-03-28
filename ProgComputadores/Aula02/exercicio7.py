import os
os.system('cls')

tc = float(input('Informe a temperatura em ºC: '))
tf = 1.8 * tc + 32
tk = tc + 273

print(f'TF = {tf:.1f}ºF n/TK = {tk:.1f}ºK')