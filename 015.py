#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

#Entrada de dados

idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso: '))
bebida = input('Bebeu nas últimas 12h[S/N]? ').strip().upper()[0]
horas_sono = int(input('Quantas horas você dormiu? '))

#Retorno de dados

if idade >= 16 and idade <= 69 and peso >= 50 and bebida == 'N' and horas_sono >= 5:
    print('Pode doar!')
else:
    print('Não pode doar!')