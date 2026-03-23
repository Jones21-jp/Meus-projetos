#Operações Matemáticas
'''
print('Olá Mundo!')
print(32 + 63)
print(76 - 37)
print(325 * 33)
print(88 / 9)
print(9 ** 9)


#Vairiável Interna

idade = 24
nome = 'João Pedro'

print(idade)
print(nome)

print(f'Seu nome é {nome}, e sua idade é {idade}')


#Variáveis Externas

nome = input('Digite seu nome:')

print(f'Seu nome é {nome}')


#Escreva um programa que leia 2 idades e retorne a soma delas

idade_1 = int(input('Digite primeira idade:'))
idade_2 = int(input('Digite segunda idade:'))

print(f'A soma das idades é {idade_1 + idade_2}')

#Strings

senai = 'Luis Eulálio'

#Fatiamento
print(senai[0])
print(senai[3:9])
print(senai[:7])
print(senai[3:])

#Análise
print(len(senai))
print(senai.count('l'))
print(senai.find('l'))
print(senai.rfind('l'))



#Transformação
print(senai.upper())
print(senai.lower())
print(senai.capitalize())
senai_novo = senai.replace('L','S')



#Condicionais

altura = float(input('Altura: '))

if altura >1.2:
    print(f'Pode andar no brinquedo!')
else:
    print(f'Quem sabe ano que vem!')

altura = float(input('Altura: '))
peso = float(input('Peso: '))

#E - and
#OU - or

if altura > 2 and peso < 200:
    print('Você vai bater a cabeça!')
elif altura < 1.2 and peso <40:
    print('Quem sabe ano que vem!')
else:
    print('Pode andar no brinquedo!')

#Importar bibliotecas

import random
pc = random.randint(1,3)
print(pc)

#for

#1
for i in  range(1, 10):
    print('*')

#2
for i in range(1,101):
    print(i)

#3
for i in  range(10,0, -1):
    print('i')

#4
soma = 0
for i in range(1, 11):
    n = int(input('N: '))
    soma = soma + n

    print(soma)



#while

#1

contador = 0

while contador < 5:
    contador += 1
    print('OI')


#2

contador = 0
resposta = 'S'

while resposta != 'N': # condição de parada
    print(f'O contador é {contador}')
    contador += 1
    resposta = str(input('Quer continuar S/N? ')).strip().upper()[0]

print('Loop concluído')
'''

#while true

#1

while True:
    n = int(input('Digite algo[999 para parar]: '))
    if n == 999:
        break

#2

while True:
    opcao = int(input('1. OI'
                      '\n2. Olá'
                      '\n3. Bem vindo'
                      '\n4. Sair ----> '))

    if opcao == 1:
        print('OI')
    elif opcao == 2:
        print('Olá')
    elif opcao == 3:
        print('Bem vindo')
    elif opcao == 4:
        print('Até logo!')
        break
#type() = retorno do valor da variavel