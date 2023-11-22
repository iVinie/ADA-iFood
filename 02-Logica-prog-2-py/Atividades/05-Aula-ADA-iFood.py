import sys

def reversao(*lista):
    lista_aux = list(lista)
    return lista_aux.reverse()

print(sys.argv)
print(reversao(*sys.argv))