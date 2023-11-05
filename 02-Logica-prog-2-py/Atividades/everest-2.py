'''
Usando Dicionário para Calcular Quadrado de Números
Dicionários são estruturas de dados muito úteis e flexíveis, podendo, inclusive, ser construídos a partir de outras estruturas, como listas.

Sabendo disso, crie uma função dicionarioQuadrados() que receba uma lista números e gera um dicionário, de forma que cada chave do dicionário seja um elemento da lista e cada valor seja este elemento ao quadrado.
'''


def dicionarioQuadrados(listaA):
    dicionario = {}
    for i in listaA:
        dicionario[i] = i**2
    return dicionario

'''
Expressões geradoras para tuplas
Também é possível utilizar expressão geradoras para construir tuplas. Sendo assim, crie a função getQuadrado() que recebe uma tupla de elementos numéricos, e retorna uma tupla com o quadrado de cada elemento da tupla original.
'''
def getQuadrado(tupla_original):
    quadrados = tuple(x**2 for x in tupla_original)
    return quadrados

'''
Da mesma forma que utilizamos a sintaxe "pythonica" de compreensão de listas, podemos fazer uma estrutura semelhante para gerar dicionários. Sendo assim, crie uma função mediaAlunosParaDicionario() que receba uma lista de listas, em que o primeiro elemento é uma lista com os nomes dos alunos; e o segundo elemento é uma lista com suas respectivas médias. Utilizando compreensão de dicionários, armazene estes dados no dicionário de forma que cada aluno seja a chave e sua média seja o valor.

OBS: caso a nota não esteja numérica, é necessário tratar os valores para tipos numéricos!
'''
def mediaAlunosParaDicionario(listaAlunos):
    nomes = listaAlunos[0]
    medias = listaAlunos[1]
    
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    medias_numericas = [float(media) if is_float(media) else 0.0 for media in medias]

    dicionario = {nomes[i]: medias_numericas[i] for i in range(len(nomes))}

    return dicionario

'''
Dicionário cujos valores são listas
Em determinadas situações, é necessário agrupar informações de acordo com alguma dada característica para facilitar o acesso a essas informações. Uma estrutura em python que armazena informações seguindo essa organização são dicionários.

Um exemplo de uso comum de dicionários são cadastros de clientes, em que, por exemplo, um elemento do dicionário pode ser o nome dos clientes, outro elemento o emprego outro o estado de habitação. Quando quisermos utilizar apenas as informações de estado, selecionamos apenas este elemento do dicionário, utilizando a respectiva chave como indexador do dicionário.

Sabendo disso, crie uma função mediaPrecoCelular() que receba um dicionário que possui a chave "valor", e retorne uma lista com: a média dos valores existentes nesta chave, o celular mais barato, e o mais caro, nesta ordem.
'''

def mediaPrecoCelular(dicionario):
    valores = dicionario.get("valor", [])  
    
    if not valores:
        return [0, None, None] 

    media = sum(valores) / len(valores)  
    mais_barato = min(valores)  
    mais_caro = max(valores)  

    return [media, mais_barato, mais_caro]


'''
Muitas vezes quando estamos trabalhando com strings, pode ser bem útil usarmos compreensão de listas para processar caractere a caractere. Sabendo disso, crie uma função encontraConsoantes que retorna uma string com todas as consoantes (e apenas as consoantes!) de uma dada frase de input.
'''

def encontraConsoantes(listaStrings):
    lista = []
    for i in listaStrings:
        if (i.upper() != 'A') and (i.upper() != 'E') and (i.upper() != 'I') and (i.upper() != 'O') and (i.upper() != 'U') and i != ' ' and i != '!' and i != "," and i != '.':
            lista.append(i)
    return ''.join(lista)

'''
Filtrando elementos por funções lambda
Em programação, temos que pensar não apenas na implementação do código propriamente dita para execução correta da tarefa desejada, como também na melhor forma de realizar esta implementação. Com isso, paradigmas de programação foram criados para auxiliar o programador a pensar diferente.

Um desses paradigmas é a programação funcional, cujo objetivo é aumentar o determinismo do programa de forma que, caso o programa seja escalável e se torne muito grande, os desenvolvedores não percam o controle do código. Uma forma de fazer programação funcional é por meio de funções lambdas, também conhecidas como "funções anônimas", tendo esse nome porque não precisam ser declaradas com um nome.

Sabendo disso, crie uma função filtraElementos() que recebe uma lista e utiliza função lambda para filtrar os elementos maiores que 10, ou seja, a função deve retornar uma lista apenas com estes elementos maiores que 10.

OBS: em um cenário real, a função filtraElementos() seria utilizada para outras funcionalidades também além da utilização da lambda, de forma a melhorar o determinismo do código.
'''


def filtraElementos(listaA):
    elementos_filtrados = list(filter(lambda x: x > 10, listaA))
    return elementos_filtrados

'''
Encontrando números divisíveis por 7
Uma forma "pythonica" de iterarmos por listas é por meio de compreensão de listas, que substitui o uso de um laço de repetição for tal como implementamos tradicionalmente para a criação de novas listas.

Sabendo disso, digamos que em um sistema desejemos buscar, entre 1000 usuários, apenas aqueles cujo ID é divisível por 7. Faça uma função numerosDiv7() para este sistema que receba uma lista A de 1000 elementos e retorne uma lista apenas com os elementos de A que são divisíveis por 7.

OBS: Caso existam elementos repetidos na lista, a saída deverá exibir apenas os elementos únicos divisíveis por 7. E se não houver elementos divisíveis por 7, o programa deve retornar uma lista vazia.
'''
def numerosDiv7(listaA):
	lista = []
	for i in listaA:
		if i % 7 == 0:
			lista.append(i)
	return lista.sort()


'''
Remoção de espaços extras de strings
É comum em sistemas de cadastro, os clientes preencherem dados com caracteres ou espaços indesejáveis. Sendo assim, implemente uma função remove_espaco(listaStrings) que recebe uma lista de strings e retire espaços extras que possam haver no início, meio ou no fim de uma string.

Por exemplo,

entrada: ["  string", "  exemplo  ", "do   exercício"] saída: ["string", "exemplo", "do exercício"]
'''

def remove_espacos(listaStrings):
    resultado = []
    for string in listaStrings:
        string_sem_espacos = string.strip()
        partes = string_sem_espacos.split()
        string_sem_espacos = " ".join(partes)
        resultado.append(string_sem_espacos)
    return resultado
