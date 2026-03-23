'''
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez
'''

#Entradad de dados

frase = input('Digite sua frase:').strip()

frase = frase.replace('A' ,'a')
frase = frase.replace('á' ,'a')
frase = frase.replace('â' ,'a')
frase = frase.replace('ã' ,'a')
frase = frase.replace('à' ,'a')

#Retorno dos dados

print(f'Quantos As: {frase.count("a")}\n'
      f'Primeiro A: {frase.find('a') + 1}\n'
      f'Ultimo A: {frase.rfind('a') + 1}')



