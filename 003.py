#Escreva um programa que leia o nome, depois o sobrenome, e retorne para o usuário

#Entrada de dados

nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')

#Retorno dos dados

#print(f'Seu nome completo é {nome} {sobrenome}')

nome_completo = nome + ' ' + sobrenome
print(f'Seu nome completo é {nome_completo}')