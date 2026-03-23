#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar. No final mostre:

#1. Qual é o total gasto na compra
#2. Quantos produtos custam mais de R$1000,00
#3. Qual é o produto mais barato

total = 0
custam_mais_q_1000 = 0
mais_barato = None


while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('informe o preço R$'))
    print(f'{produto} sai por R${round(preco, 2)}')
    continuar = input('Quer continuar?S/N ').strip().upper()[0]
    total += preco
    if preco > 1000:
        custam_mais_q_1000 += 1
    elif preco < 1000:
        mais_barato = produto
    if continuar == 'N':
        print(f'O total foi R${total} e tiveram {custam_mais_q_1000} produtos que custam mais que R$1000.00 e o mais barato é {mais_barato}')
        break