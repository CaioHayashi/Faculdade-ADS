import os
os.system("cls" if os.name == "nt" else "clear")

while True:
    print()
    print('Conversão para um número decimal')
    print("[1] - menu")
    print("[2] - sobre")   

    nav = input('Escolha uma opção: ')
    match(nav):
        case '1':
            print()
            print("[1] - binário")
            print("[2] - hexadecimal")
            print("[3] - octal")

            match (input("Deseja fazer qual conversão? ")):
                case "1":
                    print("[1] binário")

                    binario = input('Digite um número binário: ').upper()
                    decimal = 0
                    n = len(binario) - 1
                    dig = '0123456789ABCDEF'

                    for i in binario:
                        decimal += dig.find(i) * 2 ** n
                        n -= 1

                    print(f'o número binário {binario} convertido para decimal é: {decimal}')

                case "2":
                    print("[2] hexadecimal")

                    hexadecimal = input('Digite um número hexadecimal: ').upper()
                    decimal = 0
                    n = len(hexadecimal) - 1
                    dig = '0123456789ABCDEF'

                    for i in hexadecimal:
                        decimal += dig.find(i) * 16 ** n
                        n -= 1

                    print(f'o número hexadecimal {hexadecimal} convertido para decimal é: {decimal}')

                    
                case "3":
                    print("[3] octal")

                    octal = input('Digite um número octal: ').upper()
                    decimal = 0
                    n = len(octal) - 1
                    dig = '0123456789ABCDEF'

                    for i in octal:
                        decimal += dig.find(i) * 8 ** n
                        n -= 1
                        
                    print(f'o número octal {octal} convertido para decimal é: {decimal}')
                    
                case _:
                    print("Opção inválida!")
                    continue

        case '2':
            print("[2] - sobre")
            print('Análise e Desenvolvimento de Sistemas \nProgramação para Computadores \n\nCaio Tsuyoshi Hayashi - 32784601\nJosé Anderson do Nascimento da Silva - 33894892\nLeonardo Amorim Bernardo\nFelipe Moraes dos Santos - 33894663 \nDavid')
            if input('Voltar? ') in 'sS':
                continue
            else:
                break

        case _:
            print("Opção inválida")
            continue

    if input('Deseja continuar? ') in 'nN':
        break

