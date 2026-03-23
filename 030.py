#Crie um programa para jogar par ou ímpar com o usuário,
#e só pare quando perder.
# Ao final deve mostrar a quantidade de vitórias
'''
import random
pc = random.randint(1, 10)
j = str(input('Qual sua escolha Par/Impar? ')).strip().upper()[0]
par = 'P'
impar = 'I'
n = int(input('Número[1/10]: '))

while n < 0 or n > 10:
    n = int(input('Número[1/10]: '))

print(f'Sua escolha é {n}')
print(f'Adversário é {pc}')
soma = n + pc
vitorias = 0

if j == par:
    pc = impar
elif j == impar:
    pc = par
if soma % 2 == 0:
    print(f'{soma} é Par')
elif soma % 2 == 1:
    print(f'{soma} é Impar')

while True:
    if soma % 2 == 0 and j == par and pc != par:
        print('Você venceu!')
        vitorias += 1
        j = str(input('Qual sua escolha Par/Impar? ')).strip().upper()[0]
        n = int(input('Número[1/10]: '))
        while n < 0 or n > 10:
            n = int(input('Número[1/10]: '))
        pc = random.randint(1, 10)
        print(f'Sua escolha é {n}')
        print(f'Adversário é {pc}')
        soma = n + pc
        if j == par:
            pc = impar
        elif j == impar:
            pc = par
        if soma % 2 == 0:
            print(f'{soma} é Par')
        elif soma % 2 == 1:
            print(f'{soma} é Impar')
    elif soma % 2 == 1 and j == impar and pc != impar:
        print('Você venceu!')
        vitorias += 1
        j = str(input('Qual sua escolha Par/Impar? ')).strip().upper()[0]
        n = int(input('Número[1/10]: '))
        while n < 0 or n > 10:
            n = int(input('Número[1/10]: '))
        pc = random.randint(1, 10)
        print(f'Sua escolha é {n}')
        print(f'Adversário é {pc}')
        soma = n + pc
        if j == par:
            pc = impar
        elif j == impar:
            pc = par
        if soma % 2 == 0:
            print(f'{soma} é Par')
        elif soma % 2 == 1:
            print(f'{soma} é Impar')
    else:
        print('Você Perdeu!')
        print(f'Número de Vitórias {vitorias}')
    break
    '''

import random
pc = random.randint(1, 10)
vitorias = 0

while True:
    print('-----------------------------------------------')
    escolha = input('Par ou Impar: [P/I]: ').strip().upper()[0]
    j = int(input('Digite um número entre 1 e 10: '))

    while j < 1 or j > 10:
        j = int(input('Digite um número entre 1 e 10: '))

    if ((pc + j) % 2 == 0 and escolha == 'P') or ((pc + j) % 2 != 0 and escolha == 'I'):
        print('Você ganhou!!')
        vitorias += 1
    else:
        print('Você Perdeu!!')

