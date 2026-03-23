#Crie um programa que leia vários números inteiros.
#O programa só vai parar quando o usuário digitar 0000.
#No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

numeros_digitados = 0
soma = 0

while True:
    n = input('Número: ')
    if n == '0000':
        print(f'Foram digitados {numeros_digitados} números')
        print(f'A soma desses números é {soma}')
        print('Até mais!')
        break

    soma += int(n)
    numeros_digitados += 1