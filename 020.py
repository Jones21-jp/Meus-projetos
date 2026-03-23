#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

numero = int(input('Digite o número:'))

for x in range(11):
    print(f'{numero} X {x} = {numero * x}')
    #tabuada = numero * x

    #print(tabuada)
