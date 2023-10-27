#01- Faça um programa que pede para o usuário digitar um número e responde se o número é positivo ou negativo.
""""""
numero = float(input('Digite um número: '))

if numero < 0:
    print(f'Número negativo: {numero}')
else:
    print(f'Número positivo: {numero}')
    
#02-Faça um programa que pede para a usuária digitar um número e responde se o número é par ou ímpar.

par_impar = int(input('Digite um número: '))

if par_impar % 2 == 0:
    print(f'Número é par: {par_impar}')
else:
    print(f'Número é ímpar: {par_impar}')

"""
03-Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool
Menos que 20 litros, desconto de 3% por litro a partir de 20 litros, desconto de 5% por litro

Gasolina
Menos que 20 litros, desconto de 4% por litro a partir de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que:

Preço do litro da gasolina é R$5,39

Preço do litro do álcool é R$4,89    
"""

opcao = input('Qual combustivel deseja colocar? \n(G-Gasolina\nA-Álcool)')
litros = float(input('Quantos litros deseja colocar? '))

match opcao.upper():
    case 'G':
        if litros < 20:
            preco = litros*5.39*0.96
            print(f'Preço total: R${preco}')
        else:
            preco = litros*5.39*0.94
            print(f'Preço total: R${preco}')
    case 'A':
        if litros < 20:
            preco = litros*4.89*0.97
            print(f'Preço total: R${preco}')
        else:
            preco = litros*4.89*0.95
            print(f'Preço total: R${preco}')
    case _:
        print('Opção invalida!')
        
        
"""
    Exercicio proposto aula 02
01-Faça um programa que deverá pedir as 2 notas de uma aluna e calcular sua média. Considere que as notas serão de 0 a 100.

O programa deverá informar a média da aluna e seu status, obedecendo as regrinhas abaixo:

Aprovada, caso a média seja pelo menos 70.

Exame, caso a média seja pelo menos 30 e menor do que 70.

Reprovada caso a média seja inferior a 30.


02-Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

- telefonou para a vítima?
- esteve no local do crime?
- mora perto da vítima?
- devia para a vítima?
- já trabalhou com a vítima?

o programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "suspeita", entre 3 e 4 como "cúmplice" e 5 como "assassino". Caso contrário, ele será classificado como "inocente"
"""


