cont = 0

while cont < 10:
    nome = input('Qual o nome do aluno? ')
    nota1 = int(input(f'Digite a 1ª nota do aluno {nome}'))
    nota2 = int(input(f'Digite a 2ª nota do aluno {nome}'))
    media = (nota1 + nota2) / 2
    
    print(f'A média do aluno {nome} é {media:.2f}')