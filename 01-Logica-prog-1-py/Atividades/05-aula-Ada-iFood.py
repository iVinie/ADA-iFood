'''
Crie um código para apoiar os alunos de uma turma a calcularem a média de suas notas com base na quantidade de provas que foram realizadas.
Solicite do usuário a quantidade de provas realizada e a nota de cada prova realizada, caso o usuário informe uma quantidade menor ou igual a 0, retorne uma msg e peça novamente.
Por fim a saída deverá contemplar uma listas com todas as nostas de provas, informando a quantidade de notas passadas e a média final. Caso a média final seja maior ou igual a 60 informe ao aluno que ele foi aprovado, caso contrário reprovado.
'''
quantidade_notas = int(input('Quantas provas você fez? '))

while quantidade_notas <= 0:
    quantidade_notas = int(input('Valor invalido! Quantas provas você fez? '))
cont = 0
notas = []
while quantidade_notas > cont:
    cont += 1
    nota = float(input(f'Qual a {cont}º nota: '))
    notas.append(nota)
if len(notas) > 0 and sum(notas)/len(notas) >= 60:
    print(f'Aprovado!\nMédia: {sum(notas)/len(notas)}\nQuantidade de provas: {quantidade_notas}\nNotas: {notas}')
else:
    print(f'Reprovado!\nMédia: {sum(notas)/len(notas)}\nQuantidade de provas: {quantidade_notas}\nNotas: {notas}')


'''
Faça um algoritmo que recebe uma lista encadeada de números inteiros e retorna uma lista ordenada sem repetições, ou seja, uma lista onde cada número apareça apenas uma vez. Exemplo:

12, 5, -7, 8, 5, 9, 12, 1, 8
resposta: 12, 5, -7, 8, 9, 1
'''
lista = [12, 5, -7, 8, 5, 9, 12, 1, 8]
cont = 0
lista_unica = []
lista_rep = []
while len(lista) > cont:
    if lista[cont] not in lista_unica:
        lista_unica.append(lista[cont])
    else:
        lista_rep.append(lista[cont])
    cont += 1
print(f'Lista com valores únicos: {lista_unica}')

'''
Agora, considere que as saídas do exercício anterior devam ser:

Lista ordenada com valores únicos
Lista apenas com os valores repetidos
'''
print(f'Lista ordenada com valores únicos: {lista_unica.sort}')
print(f'Lista com valores repetidos: {lista_rep}')

'''
Crie um código que receba um número a ser pesquisado em uma lista simples (não aninhada). Esse código deve ser removido da lista, considere que o código informado possa estar na lista representado como string ("1") ou int (1), ou seja, independente da representação ele deve ser removido. No final, retorne a lista resultante sem o código.
'''
lista_remove = ["1", 1, 456,29485,2845, 1, "1"]
lista_nova = []
remove = 1
cont = 0
while len(lista_remove) > cont:
    if not (int(remove) == lista_remove[cont] or str(remove) == lista_remove[cont]):
        lista_nova.append(lista_remove[cont])
    cont += 1
print(f'Lista inicial: {lista_remove}\nRemover: {remove}\nLista nova: {lista_nova}')
