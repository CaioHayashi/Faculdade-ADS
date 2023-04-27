mb = float(input('Digite o tamanho do arquivo em (MB): '))
mbps = float(input('Digite a velocidade do link de internet (Mbps): '))

tempo = mb * 8 / mbps
minutos =  tempo // 60
segundos = tempo % 60

print(f'Tempo aproximado para download: {minutos} minutos e {segundos} segundos')