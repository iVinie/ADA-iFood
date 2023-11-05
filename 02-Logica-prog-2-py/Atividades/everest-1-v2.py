'''
Quando utilizamos listas, uma das vantagens é que podemos adicionar novos elementos com o passar do tempo. Podemos inserir elementos tanto ao final da lista, como também em uma posição específica.

Sabendo disso, faça uma função adicionarElemento() que recebe uma lista de números e insere o número inteiro 42 no meio da lista (isto é, em sua posição central). Note que a posição de inserção pode variar a depender da quantidade de elementos na lista original.
'''


def adicionarElemento(listaA):
    quantidade = len(listaA)
    if quantidade%2 == 0:
        listaA.insert(quantidade/2, 42)
    else:
        listaA.insert(int(quantidade/2), 42)
        
    return listaA


'''
Função zip
Em programação, podemos fazer uso de diferentes listas para armazenar nossos dados para, posteriormente, unir informações destas listas. Por exemplo, podemos guardar em uma lista os nomes de funcionários de uma empresa e, em outra lista, os cargos que estes funcionários ocupam.

funcionarios = ["Paulo", "Andrea", "Marta"]
profissao = ["cientista de dados", "engenheiro de dados", "desenvolvedor"]
Dado essas duas listas, podemos querer exibir as duas informações conjuntamente da seguinte forma:

[('Paulo', 'cientista de dados'), ('Andrea', 'engenheiro de dados'), ('Marta', 'desenvolvedor')]
Podemos fazer isto por meio da função zip que recebe as duas listas e retorna uma saída como exposta acima. Além de exibir os valores, podemos fazer uso da função zip para diversas funcionalidades. Sabendo disso, crie uma função ultimoElementoLista2D() que receba uma lista de duas dimensões (isto é, uma lista de listas, na forma de matriz) e utilize o zip para retornar o último elemento de cada sublista.

Por exemplo, se tivermos a lista abaixo:

[[192, 193, 194],
 [507, 508, 509],
 [526, 527, 528, 529],
 [560, 561],
 [635, 636, 637]]
Retorne [194, 509, 529, 561, 637].
'''


def ultimoElementoLista2D(lista_2d):
    # Use a função zip para percorrer as sublistas e pegar o último elemento de cada uma
    return [sublista[-1] for sublista in lista_2d]

# Exemplo de uso
lista_2d = [[192, 193, 194],
            [507, 508, 509],
            [526, 527, 528, 529],
            [560, 561],
            [635, 636, 637]]

resultado = ultimoElementoLista2D(lista_2d)
print(resultado)


'''
Remover elementos de listas
Considere que uma empresa desenvolveu uma aplicação que solicita ao usuário uma dada informação, como, por exemplo, o segundo nome deste usuário. O programa recebe essa informação e armazena em uma lista de strings. Entretanto, caso um usuário acidentalmente não tenha preenchido esta informação, a lista conterá elementos vazios. Por exemplo, dada uma lista com 5 nomes: listaDeNomes = ['Araújo', 'Alexandre', 'Silva', 'Flávio', ''], note que o último elemento da lista é apenas uma string vazia representada pelas aspas vazias.

Sabendo disso, faça uma função removerElementosVazios() que recebe uma lista de nomes e retorna a lista sem os elementos vazios.
'''

def removerElementosVazios(listaA):
	for i in listaA:
		if '' in listaA:
			listaA.remove('')
	return listaA


'''
Indexação de listas e último elemento
Uma lista possui n elementos, sendo comum executarmos determinadas ações em um elemento de determinada posição. Por exemplo, podemos substituir o elemento da primeira posição da lista por outro valor desejado. Quando selecionamos um elemento, chamamos isto de indexação.

Sendo assim, escreva uma função ultimoElemento() em python que recebe uma lista e retorna o último elemento da lista.
'''

def ultimoElemento(listaA):
	return listaA[-1]
