#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
'''
1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

num_1 = int(input('Digite o primeiro valor: '))
num_2 = int(input('Digite o segundo valor: '))
num_3 = int(input('Digite o terceiro valor: '))
menu = 0

while True:
    print('1. Somar\n'
          '2. Multiplicar\n'
          '3. Maior\n'
          '4. Novos números\n'
          '5. Sair do programa')
    menu = int(input('Digite a escolha: '))
    if menu == 1:
        print(f'O resultado da soma é {num_1 + num_2 + num_3}')
    elif menu == 2:
        print(f'O resultado da multiplicação é {num_1 * num_2 * num_3}')
    elif menu == 3:
        if num_1 > num_2 and num_1 > num_3:
            print(f'O maior é {num_1}')
        elif num_2 > num_3:
            print(f'O maior é {num_2}')
        else:
            print(f'O maior é {num_3}')
    elif menu == 4:
        num_1 = int(input('Digite o primeiro novo valor: '))
        num_2 = int(input('Digite o segundo novo valor: '))
        num_3 = int(input('Digite o terceiro novo valor: '))
    elif menu == 5:
        print('Até mais!')
        break

