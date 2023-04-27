print('Pousada do Jobs')
print('[S] simples')
print('[D] duplo')
print('[T] triplo')

opcao = input('Digite o tipo de hospedagem: ')
diarias = int(input('Digite o número de diárias: '))

if opcao in 'sS':
    print(f'O valor é de {diarias * 255.5}')
elif opcao in 'dD':
    print(f'O valor é de {diarias * 305.5}')
elif opcao in 'tT ':
    print(f'O valor é de {diarias * 360.5}')
else:
    print('Opção incorreta, tente novamente ')

