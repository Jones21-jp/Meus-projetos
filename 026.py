#Faça um programa que leia um número e retorne o fatorial !

#4! = 4 x 3 x 2 x 1

num = int(input('Número: '))
fatorial = 1
contador = num

while contador > 0:
    fatorial *= contador
    contador -= 1
print(f'O fatorial de {num} é {fatorial}')