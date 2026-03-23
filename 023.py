#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''
#Entrada de dados

maior_peso = 0
menor_peso = 9999
maior = ''
menor = ''

#Manipulação dos dados

for i in range(1, 7):
    print(f'Pessoa {i}')
    nome = input('Digite seu nome: ')
    peso = float(input('Digite o seu peso: '))

    if peso > maior_peso:
        maior = nome
        maior_peso = peso
    if peso < menor_peso:
        menor = nome
        menor_peso = peso

#Retorno dos dados

print(f'{maior} tem o maior peso {maior_peso}')
print(f'{menor} tem o menor peso  {menor_peso}')
'''

#Entrada de dados

maior_peso = None
menor_peso = None

#Manipulação dos dados

for i in range(7):
    peso = float(input('Peso: '))
    if maior_peso == None and menor_peso == None:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

#Retorno dos dados

print(f'O maior peso é {maior_peso}'
      f'\nO menor peso é {menor_peso}')





