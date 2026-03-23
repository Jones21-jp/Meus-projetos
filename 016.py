#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random



pc = random.randint(1, 3)
j = int(input('Digite a sua escolha:'
              '\n1. Pedra'
              '\n2. Papel'
              '\n3. Tesoura ------> '))

if pc == j:
    print('Empate')
elif(pc == 1 and j == 2) or (pc == 2 and j == 3) or (pc == 3 and j == 1):
    print(f'Vitória - J {j} x {pc} PC')
else:
    print(f'Derrota - J {j} x {pc} PC')

