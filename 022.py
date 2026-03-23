'''
#Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

1. A média de idade do grupo
2. Qual é o homem mais velho
3. Quantas mulheres têm menos de 20 anos
'''
'''
#Entrada de dados
soma = 0
idade_homem_mais_velho = 0
mulheres_com_menos_20 = 0
homem_mais_velho = ''

#Manipulação dos dados

for i in range(1, 5):
    print(f'Pessoa {i}')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
    soma = soma + idade

    if sexo == 'F' and idade < 20:
        mulheres_com_menos_20 = mulheres_com_menos_20 + 1

    if sexo == 'M' and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade

média = soma / 4

#Retorno dos dados

print(f'A média das idades é: {int(média)}')

if homem_mais_velho != '':
    print(f'O homem mais velho é o {homem_mais_velho} com {idade_homem_mais_velho} anos')
else:
    print(f'Não há homens no grupo')
if mulheres_com_menos_20 > 0:
     print(f'Há {mulheres_com_menos_20} mulher com menos de 20 anos no grupo')
elif mulheres_com_menos_20 == 0:
     print(f'Não há mulheres com menos de 20 anos no grupo')
else:
     print(f'Não há mulheres no grupo')
'''

#Entrada de dados

soma = 0
i_h_m_v = 0
n_h_m_v = ''
q_m_m_20_anos = 0

for i in range(4):
    nome = input('Nome: ')
    idade = int(input('idade: '))
    sexo = input('Sexo[M/F]: ').strip().upper()[0]
    #1
    soma = soma + idade
    #2
    if sexo == 'M' and idade > i_h_m_v:
        i_h_m_v = idade
        n_h_m_v = nome
    #3
    if sexo == 'F' and idade < 20:
        q_m_m_20_anos = q_m_m_20_anos + 1

print(f'A média de idade é {soma/4}'
      f'\na quantidade de mulheres com menos de 20 anos é {q_m_m_20_anos}'
      f'\no homem mais velho é {n_h_m_v}')

