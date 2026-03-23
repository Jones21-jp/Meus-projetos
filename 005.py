#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

#Entrada de dados

raio = float(input('Digite o raio:'))

#Manipulação dos dados

Volume_da_Esfera = (4/3) * 3.1415 * raio ** 3
Área_da_Esfera = 4 * 3.1415 * raio ** 2

#Retorno dos dados

print(f'O Volume da Esfera é {round(Volume_da_Esfera, 2)}\nÁrea é {round(Área_da_Esfera, 2)}')
#print(f'Área da Esfera é {Área_da_Esfera}')