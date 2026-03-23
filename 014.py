#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

#Entrada de dados

letra = input('Informe uma letra:').strip().lower()[0]

if letra in 'aeiouAáàãâEéèêIíìîOóòõôUùúû':
    print('É vogal.')
else:
    print('É consoante.')