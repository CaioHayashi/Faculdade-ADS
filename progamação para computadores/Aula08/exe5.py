import math

turmas = int(input('Digite a quantidade de turmas: '))

soma = 0

for i in range(turmas):
    alunos = int(input(f'Digite a quantidade de alunos da {1+i}ª turma: '))
    soma += alunos

media = soma / turmas

print(f'As turmas têm em média {math.ceil(media)} alunos')