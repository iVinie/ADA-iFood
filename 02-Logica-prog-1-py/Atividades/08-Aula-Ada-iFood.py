#Calculadora
def calc(num1, num2, sinal):
    match sinal:
        case '+':
            return f'A soma foi: {num1 + num2}'
        case '-':
            return f'A subtração foi: {num1 - num2}'
        case '*':
            return f'A multiplicação foi: {num1 * num2}'
        case '/':
            if num2 == 0:
                return 'Não pode dividir por zero'
            return f'A divisão foi: {num1 / num2}'
        case _:
            return 'Operação invalida'

sinal = input('Qual a operação? (+, -, *, /): ')
num1 = float(input('Qual o primeiro número: '))
num2 = float(input('Qual o segundo número: '))
resultado = calc(num1, num2, sinal)
print(resultado)

'''
Crie uma função chamada contar_palavras que recebe uma string como argumento e retorna uma lista com as palavras únicas e uma lista com a contagem de quantas vezes cada palavra aparece na string. Considere que as palavras são separadas por espaços e que a capitalização das palavras não deve afetar a contagem (ou seja, "Python" e "python" devem ser considerados iguais).
'''

def contar_palavras(frase):
    frase = frase.lower()
    palavras = frase.split()
    unicas = []
    qtd_palavras = []
    for palavra in palavras:
        if palavra not in unicas:
            unicas.append(palavra)
            qtd_palavras.append(1)
        else:
            indice = unicas.index(palavra)
            qtd_palavras[indice] += 1 
    return unicas, qtd_palavras

frase = "o mar é Azul pq o ceu é azul"
unicas, qtd_palavras = contar_palavras(frase)
print(frase)
for i in range(0, len(qtd_palavras)):
    print(f'{unicas[i]} -> {qtd_palavras[i]}')

'''
DESAFIO
Você é encarregado de criar um sistema de gerenciamento de estoque de uma loja. Crie funções para as seguintes operações:

Adicionar um novo produto ao estoque.
A função deve receber o nome do produto, a quantidade em estoque e o preço unitário.

Exibir um resumo do estoque, incluindo o nome do produto, a quantidade em estoque e o valor total para cada produto.

Crie um menu interativo que permita ao usuário realizar essas operações. O usuário deve poder adicionar novos produtos, atualizar quantidades e visualizar o resumo do estoque. Use funções para organizar o código.
'''
