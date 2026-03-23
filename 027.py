#Escreva um programa que leia um número n inteiro qualquer
#e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

num = int(input('Número: '))
a, b = 0, 1
contador = 0

while contador < num:
    print(a, end=' ')
    p = a + b
    a = b
    b = p
    contador += 1