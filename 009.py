#Crie um programa que leia um nome, e mostre o primeiro e o último nome

#Entrada de dados

nome = input('Digite seu nome:').strip()
posicao_1_espaco = nome.find(' ')
primeiro_nome = nome[0:posicao_1_espaco]
posicao_ultimo_espaco = nome.rfind(' ')
ultimo_nome = nome[posicao_ultimo_espaco + 1:]

#Retorno dos dados

print(f'Seu nome completo é {nome}\n'
      f'Seu primeiro nome é {primeiro_nome}\n'
      f'Seu ultimo nome é {ultimo_nome}')
