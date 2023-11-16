print('Simulador de Cofre')
print('Insira a quantidade de moedas que deseja colocar respectivamente')

qtyTwentyFive = int(input('qtde de moedas de 25 centavos: '))
qtyTen = int(input('qtde de moedas de 10 centavos: '))
qtyFive = int(input('qtde de moedas de 5 centavos: '))

def safeValue(tf, t, f):
    tf = tf * 25
    t = t * 10
    f = f * 5

    total = (tf + t + f) / 100
    print(f'o total depositado é de R${total:.2f}')

safeValue(qtyTwentyFive, qtyTen, qtyFive)