#Escreva um programa que converta real para o Franco Congolês

#Entrada de dados

real = float(input('Digite a quantidade de reais a ser convertida:'))

#Manipulação dos Dados

#franco_congo = real * 533.62

#Retorno de dados

#print(f'A conversão de R${real} para Francos Congoleses é ${franco_congo} ')

#2 metódo de resolução
print(f'A conversão de R${real} para Francos Congoleses é ${round((real * 533.62))}')