#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

#Entrada de dados

nota_1 = float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
nota_3 = float(input('Digite a terceira nota:'))
nota_4 = float(input('Digite a quarta nota:'))
nota_5 = float(input('Digite a quinta nota:'))
nota_6 = float(input('Digite a sexta nota:'))

#Manipulação dos dados

Média_do_aluno = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5 + nota_6) / 6

#Retorno dos dados

print(f'A média desse aluno foi {round(Média_do_aluno, 2)}')