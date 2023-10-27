'''
Faça um código que recebe um texto contendo letras, números e espaços. E, passando uma palavra, ele irá verificar se essa palavra existe nesse texto, retornando True ou False.

obs: A palavra precisa ser idêntica (mas pode ter capitalização diferente). Encontrar um trecho dela 'dentro' de outra palavra não deve contar como existente no texto.
'''

texto = "Eu me chamo Joao e minha linguagem de programação favorita é python desde 2023"
palavra_a_pesquisar = "linguagem"

palavras_no_texto = texto.split()
palavra_a_pesquisar = palavra_a_pesquisar.lower()
encontrada = False
for palavra in palavras_no_texto:
    if palavra.lower() == palavra_a_pesquisar:
        encontrada = True
        break
if encontrada:
    print("True")
else:
    print("False")

'''
Faça um código que recebe uma string e retorna todas as letras minúsculas com exceção da letra A/a.
Ex: recebe: Posso dizer que sei programar em Python.
retorna: posso dizer que sei progrAmAr em python.
'''
texto = 'Posso dizer que sei programar em Python.'
texto_min = texto.lower()
novo_texto = texto_min.replace('a', 'A')
print(novo_texto)

'''
Considera a população da cidade X igual 75340 habitantes, sendo que esta cidade tem uma taxa de crescimento anual de 3.7%. A cidade Y tem uma população de 213480 habitantes com uma taxa de crescimento anual de 1.7%. Faça um código que informe em quantos anos a população da cidade X ultrapassará a cidade
'''
x = 75340
y = 213480
contador = 0

while x <= y:
    contador += 1
    x *= 1.037
    y *= 1.017
    
print(f'A cidade X demorou {contador} anos para ultrapassar a Y')

'''
A série de Fibonacci é uma sequência matemática que começa com 0 e 1, e os números subsequentes são a soma dos dois números anteriores. A sequência começa da seguinte forma:<br>
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...<br>
Faça um programa que gere a série até que o valor seja maior que um valor informado pelo usuário. Informe quando o valor ultrapassar o valor informado pelo usuário.
'''

valor = int(input('Qual valor final da série de Fibonacci: '))
atual = 1
anterior = 0
lista_fib = []
lista_fib.append(anterior)
while atual <= valor:
    lista_fib.append(atual)
    proximo = atual + anterior
    anterior = atual
    atual = proximo
print(f'A série de Fibonacci é: {lista_fib} e o número digitado: {valor}')