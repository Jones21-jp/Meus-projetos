'''
#Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''

#Entrada de dados
nome = input('Digite seu nome:').strip()
quantidades_letras_s_espaco1 = len(nome) - nome.count(' ')
posicao_1_espaco = nome.find(' ')
primeiro_nome = nome[0:posicao_1_espaco]
quantidades_letras_1_nome = len(primeiro_nome)

#Retorno dos dados
print(f'Maiusculas: {nome.upper()}\n'
      f'Minusculas: {nome.lower()}\n'
      f'Quantidades de Letras sem espaço: {quantidades_letras_s_espaco1}\n'
      f'Quantidades de Letras 1 nome: {quantidades_letras_1_nome}')

