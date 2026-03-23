#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.

#Entrada de dados

import random

pc = random.randint(1, 10)
j = int(input('Adivinhe o número entre [1:10]: '))
while j < 1 or j > 10:
    print('Digite entre 1 e 10!')
    j = int(input('Adivinhe o número entre [1:10]: '))
tentativas = 0

while j != pc:
    pc = random.randint(1, 10)
    print(f'O número era {pc}')
    tentativas += 1
    j = int(input('Tente novamente: '))
    while j < 1 or j > 10:
        print('Digite entre 1 e 10!')
        j = int(input('Adivinhe o número entre [1:10]: '))

print(f'Você acertou!'
      f'\nNúmero de tentativas: {tentativas}')