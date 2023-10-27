#1
def melhores_alunos(lista):
    total_notas = sum(aluno['nota'] for aluno in lista)
    media_turma = total_notas / len(lista)
    alunos_acima_da_media = [aluno['nome'] for aluno in lista if aluno['nota'] >= media_turma]
    return alunos_acima_da_media
print(melhores_alunos([{ "nome": "Maria", "nota": 7 },{"nome": "Marta", "nota": 5 },{"nome": "Marcia", "nota": 5.5 }]))  # Resultado: ["Maria"]
print(melhores_alunos([{ "nome": "Joao", "nota": 7 },{"nome": "Lucas", "nota": 5 },{"nome": "Maria", "nota": 0 },{"nome": "Marcia", "nota": 5.5 }]))  # Resultado: ["Joao", "Lucas", "Marcia"]

#2
def soma_algarismos(numero):
    if numero <= 0:
        return -1
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

print(soma_algarismos(235))  # Resultado: 10
print(soma_algarismos(121))  # Resultado: 4
