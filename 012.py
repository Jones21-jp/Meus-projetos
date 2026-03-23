#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

#Entrada de dados

numero = int(input('Informe um número:'))

#Retorno de dados

if numero % 2 == 0:
    print(f'{numero} é Par!')
else:
    print(f'{numero} é ímpar!')