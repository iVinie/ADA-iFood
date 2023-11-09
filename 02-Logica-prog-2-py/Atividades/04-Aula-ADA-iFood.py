'''
Usando expressões geradoras, faça um programa em python que receba uma frase, e crie uma expressão geradora que retorne apenas as palavras que comecem com a letra "a". Imprima o resultado iterando do gerador.
'''

frase = input("Digite uma frase a ser analisada: ")
gerador = (f'Palavra: {palavra}' for palavra in frase.split() if palavra[0].lower() == 'a')
for palavra_rotulada in gerador:
    print(palavra_rotulada)



'''
Usando funções geradoras, faça um programa em python que receba uma frase, e crie uma função geradora que retorne apenas as palavras que comecem com a letra "a". Imprima o resultado iterando do gerador.
'''

def geradora_palavra(frase):
    palavras = frase.split() 
    for palavra in palavras:
        if palavra.lower().startswith('a'): 
            yield palavra
frase = input("Digite uma frase: ")
gerador = geradora_palavra(frase)
for palavra in gerador:
    print(palavra)
    
'''
Faça uma função/expressão geradora em python que receba uma lista de alunos e uma lista de cursos, e retorne um dicionário por vez no formato:
{"nome": aluno, "curso" :curso}
'''

def gerador_alunos_cursos(alunos, cursos):
    for aluno, curso in zip(alunos, cursos):
        yield {"nome": aluno, "curso": curso}
alunos = ["Alice", "Bob", "Carol", "David"]
cursos = ["Matemática", "História", "Ciência", "Inglês"]
gerador = gerador_alunos_cursos(alunos, cursos)
for aluno_curso in gerador:
    print(aluno_curso)
