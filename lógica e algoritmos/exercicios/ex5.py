qtdeTelheiro = int(input('Digitea a quantidade de pregos telheiros'))
qtdeQuadrado = int(input('Digite a quantidade de pregos quadrados:')) 
total = qtdeTelheiro * 1.05 + qtdeQuadrado * 0.51  

comissao = total * 10 / 100  

print('Valor arrecadado:', total)
print('Comissão:', comissao)

