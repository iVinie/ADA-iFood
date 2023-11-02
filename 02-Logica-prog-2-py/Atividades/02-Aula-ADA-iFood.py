'''
Crie uma função chamada busca que receba um dicionário e um valor. A função deverá retornar uma lista com as as chaves em que o valor recebido está associado.
Exemplo:

Entrada:
dicionario = { "chave1": 4, "chave2": 5, "chave3": 5, "chave4": 1 }
valor = 5
Saída:
["chave2", "chave3"]
Em complemento, peça que o usuário informe cada chave e valor que será armazenado no dicionário, e também, qual valor ele deseja buscar pela função. O programa deverá permitir que o usuário digite 10 chaves e 10 valores e 1 valor a ser buscado.
'''
def dicionario_valor(dicionario:{}, valor):
    lista = []
    for chave, valor_dicionario in dicionario.items():
        if valor == valor_dicionario:
            lista.append(chave)
    return lista
dicionario = { "chave1": 4, "chave2": 5, "chave3": 5, "chave4": 1 }
valor = 5
lista = dicionario_valor(dicionario, valor)
print(lista)


'''
Faça uma função chamada conta_letras que receba uma frase digitada pelo usuário, e que seja capaz de contar a ocorrência de cada palavra na frase recebida. Para implementar esta função, utilize dicionários.
Exemplo:

Entrada:
frase = "Dicionários são legais!"
Saída:
d=1
i=4
c=1
o=3
...
'''
def contar_letras(frase):
    frase = frase.lower()
    unicas = {}
    for letra in frase:
        if letra not in unicas:
            if letra != ' ':
                unicas.update({letra: 1})
        else:
            unicas[letra] += 1
    return unicas

frase = "Dicionários são legais"
print(frase)
resultado = contar_letras(frase)
for letra, qtd in resultado.items():
    print(f'{letra}: {qtd}')


'''
Escreva uma função chamada contador_palavras que receba uma frase, e retorne quantas vezes cada palavra aparece neste texto. Utilize dicionários para a contagem de cada palavra
'''

def contar_palavras(frase):
    frase = frase.lower()
    palavras = frase.split()
    unicas = {}
    for palavra in palavras:
        if palavra not in unicas:
            unicas.update({palavra: 1})
        else:
            unicas[palavra] += 1
    return unicas

frase = "o mar é Azul pq o ceu é azul"
print(frase)
resultado_2 = contar_palavras(frase)
for palavra, qtd in resultado_2.items():
    print(f'{palavra}: {qtd}')
    
    
    '''
    Crie uma lista com 4 números inteiros e outra com 4 chaves (notas), e utilize a função
    zip, para criar um dicionário onde a chave seja a lista de notas e o valor a lista de números
    '''
    
def dicionario_notas(lista_numero, lista_string):
    dicionario = {}
    for chave, valor in zip(lista_string, lista_numero):
        dicionario.update({chave: valor})
    return dicionario
lista_numeros = [10, 8, 5, 7]
lista_strings = ["nota1", "nota2", "nota3", "nota4"]
dicionario = dicionario_notas(lista_numeros, lista_strings)
print (dicionario)