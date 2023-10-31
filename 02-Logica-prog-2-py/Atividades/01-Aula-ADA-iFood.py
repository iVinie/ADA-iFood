'''
1-Escreva uma função chamada intercala que recebe duas tuplas de três elementos cada e retornar uma tupla de seis elementos, intercalando as duas tuplas
exemplo:
entrada tupla1= (1, 2, 4); tupla2=(3, 5, 6)
saida: (1, 3, 2, 5, 4, 6)
'''
tupla1= (1, 2, 4)
tupla2=(3, 5, 6)
nova_tupla = []
def intercala(x, y):
    for i in range(0,3):
        nova_tupla.append(x[i])
        nova_tupla.append(y[i])
intercala(tupla1, tupla2)
nova_tupla = tuple(nova_tupla)
print(nova_tupla)

'''
2-Escreva a função chamada opera que recebe uma tupla com uma string e dois números; se a string for ’SOMA’, retorna a soma dos dois números, se for ’MULT’, retorna a multiplicação, se for ’DIV’, retorna a divisão, se for ’SUB’, retorna a subtração, se não for nenhuma das anteriores retorna None.
'''

def opera(tupla):
    match tupla[0].upper():
        case 'SOMA':
            return tupla[1] + tupla[2]
        case 'MULT':
            return tupla[1] * tupla[2]
        case 'SUB':
            return tupla[1] - tupla[2]
        case 'DIV':
            if tupla[2] == 0:
                return 'Divisão por zero'
            else:
                return tupla[1]/tupla[2]
        case _:
            return 'Operação invalida!'

tupla_soma = ('soma', 5, 5)
print(opera(tupla_soma))
tupla_mult = ('mult', 5, 5)
print(opera(tupla_mult))
tupla_sub = ('sub', 5, 5)
print(opera(tupla_sub))
tupla_div = ('div', 5, 5)
print(opera(tupla_div))
