cont = 0

while True:
    resp = input('já dormi? s/n: ')
    if resp in 'nN':
        cont += 1
    else:
        break

print(f'Você contou {cont} carneirinhos')
