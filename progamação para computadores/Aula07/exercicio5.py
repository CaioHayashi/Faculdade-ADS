import os
os.system('cls' if os.name == 'nt' else 'clear')

qtdeAlunos = 0
pesoAlunos = 0
qtdeAlunas = 0
pesoAlunas = 0

while True:
    genero = input('Digite seu genero [m/f]: ')
    peso = float(input('Digite o seu peso: '))
    if genero in 'mM':
        qtdeAlunos += 1
        pesoAlunos += peso
    elif genero in 'fF':
        qtdeAlunas += 1
        pesoAlunas += peso
    else:
        print('genero incorreto')

    if input('Continuar? [s/n]: ') in 'nN':
        break

if pesoAlunos != 0 and qtdeAlunos != 0:
    mediaAlunos = pesoAlunos / qtdeAlunos
    print(f'número de Alunos: {qtdeAlunos} peso média: {mediaAlunos}')
else:
    print('Não pode haver valor zero')
if pesoAlunas != 0 and qtdeAlunas != 0:
    mediaAlunas = pesoAlunas / qtdeAlunas
    print(f'número de Alunas: {qtdeAlunas} peso média: {mediaAlunas}')
else:
    print('Não pode haver valor zero')





