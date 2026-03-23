#Crie um programa que retorne a tabuada de um número,
#e só pare quando o número digitado for 0000

while True:
    n = int(input('Número: '))
    if n == 0000:
        print('Até mais!!')
        break
    for x in range(11):
        print(f'{n} X {x} = {n * x}')