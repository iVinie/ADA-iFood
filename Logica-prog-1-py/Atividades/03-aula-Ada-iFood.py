"""
Modifique o programa das médias do exercício anterior da seguinte maneira:

Caso a aluna tenha ficado de exame, pergunte a nota do exame.

Uma nova média deve ser calculada entre a média original e a nota do exame:

media_exame = (media + exame)/2

O programa deve exibir essa nova média junto do novo status:

Aprovada por exame caso a media_exame seja pelo menos 50.
Reprovada caso a media_exame seja inferior a 50.
"""

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
if media >= 70:
    print("aprovada")
elif media >= 30:
    print("exame")
    exame = int(input("Digite a nota do exame: "))
    media_exame = (exame + media)/2
    if media_exame >= 50:
        print("aprovada pelo exame")
    else:
        print("reprovada pelo exame")
else:
    print("reprovada")
    
    
'''
Faça um programa que recebe as coordenadas e encontra a distância entre dois pontos em um plano cartesiano (x e y)
'''

coord_x_1 = float(input('Digite o x da primeira coordenada: '))
coord_y_1 = float(input('Digite o y da primeira coordenada: '))
coord_x_2 = float(input('Digite o x da segunda coordenada: '))
coord_y_2 = float(input('Digite o y da segunda coordenada: '))


dif_x = coord_x_2 - coord_x_1
dif_y = coord_y_2 - coord_y_1

distancia = (dif_x ** 2 + dif_y ** 2) ** 0.5

print(f'A distância entre as coordenadas é de: {distancia}')


'''
Escreva um programa Python que gera um número secreto aleatório entre 1 e 100 e, em seguida, solicita ao usuário que adivinhe qual é o número. O programa deve fornecer dicas (maior/menor) após cada tentativa do usuário. O jogo deve continuar até que o usuário adivinhe corretamente o número secreto e quando adivinhar o número secreto a repetição deve ser interrompida. Registre quantas tentativas o usuário levou para acertar e exiba no final.

'''

numero = 42
num = int(input('Digite um número entre 1 e 100: '))
while num != numero:
    if num < numero:
        num = int(input('Número menor, tente novamente!: '))
    elif num > numero:
        num = int(input('Número maior, tente novamente!: '))
print('Acertou!')
        
'''
Escreva um programa em Python que solicita ao usuário inserir uma sequência de números inteiros. O programa deve continuar pedindo números até que o usuário escolha parar. Após cada número inserido, o programa deve verificar se o número é par. Se for par, incremente um contador e continue pedindo por mais números. No final, o programa deve exibir a quantidade total de números pares inseridos.
'''
contador = 0

continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um número'))
    if numero % 2 == 0:
        contador += 1
    continuar = input('Deseja continuar? (S ou qualquer tecla para sair) ').upper()
print(f'Teve {contador} números pares')

'''
Imprima os seguintes padrões utilizando loop. O usuário deverá determinar quão grande será a extensão/comprimento
padrão I:

*
**
***
****



padrão II:

*
**
***
**
*
'''


numero = int(input('Digite um número: '))
cont = 1
#padrão 1:
print('Padrão 1: ')
while cont <= numero:
    aux = '*'*cont
    print(aux)
    cont += 1


#padrão 2:
cont = 1
print('Padrão 2:')
while cont <= numero:
    aux = '*'*cont
    print(aux)
    cont += 1
    if cont == numero:
        cont = 1
        numero -= 1
        while numero >= cont:
            aux = '*'*numero
            print(aux)
            numero -= 1

'''
Faça a somatória de todos os numeros seguindo a sequência:
1/1+1/2+1/3+1/4+1/5+1/6+...+1/1000
'''
cont = 1
soma = 0
while cont <= 1000:
    soma += 1/cont
    cont += 1
print(soma)
    
'''

'''

numero = int(input("Digite um número inteiro positivo: "))



numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10

print(f"O número invertido é: {numero_invertido}")