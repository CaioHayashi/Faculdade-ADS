podemVotar = 0
somaAlunos = 0
n = 10

for i in range(n):
    idade = int(input('Digite a idade do Aluno: '))
    if idade >= 16:
        podemVotar += 1


print(f'A quantidade de alunos que podem votar é {podemVotar}')
