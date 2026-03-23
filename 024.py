#Escreva um programa que verifique se uma frase é um palíndromo.

#Entrada de dados

palavra = input('Palavra: ').strip().lower()

#1

pontos = 0
for i in range(0, len(palavra)):
    if palavra[i] == palavra[-i-1]:
        pontos = pontos + 1

    if pontos == len(palavra):
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')



#2
#f palavra == palavra[::-1]:
#    print('É um palíndromo')
#else:
#    print('Não é um palíndromo')












