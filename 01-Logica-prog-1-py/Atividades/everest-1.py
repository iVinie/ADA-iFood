#1
def primeiro_caractere_unico(palavra):
    ocorrencias = [0] * 26
    indices = [-1] * 26 
    for i, caractere in enumerate(palavra):
        indice = ord(caractere) - ord('a')
        ocorrencias[indice] += 1
        if indices[indice] == -1:
            indices[indice] = i

    primeiro_indice = len(palavra) 
    for i, caractere in enumerate(palavra):
        indice = ord(caractere) - ord('a')
        if ocorrencias[indice] == 1 and indices[indice] < primeiro_indice:
            primeiro_indice = indices[indice]

    if primeiro_indice == len(palavra):
        return -1 
    else:
        return primeiro_indice

print( primeiro_caractere_unico("amor"))   
print( primeiro_caractere_unico("cocada"))  

#2
def idade_em_dias(lista):
    anos, meses, dias = lista
    idade_em_dias = (anos * 365) + (meses * 30) + dias
    return idade_em_dias

print(idade_em_dias([5, 4, 14]))  # Resultado: 1959
print(idade_em_dias([10, 8, 16]))  # Resultado: 3906

#3
def media_aproveitamento(lista):
    N1, N2, N3, media_exercicios = lista
    media_aproveitamento = (N1 + N2 * 2 + N3 * 3 + media_exercicios) / 7

    if media_aproveitamento >= 9.0:
        return "A"
    elif media_aproveitamento >= 7.5:
        return "B"
    elif media_aproveitamento >= 6.0:
        return "C"
    else:
        return "D"

print(media_aproveitamento([8.0, 7.0, 8.0, 8.0]))  # Resultado: "B"
print(media_aproveitamento([5.0, 4.3, 8.0, 7.0]))  # Resultado: "C"

#4
def calculo_salario_com_comissao(lista):
    num_carros_vendidos, valor_total_vendas, salario_fixo, valor_fixo_por_carro = lista
    comissao_valor_total = 0.05 * valor_total_vendas
    comissao_por_carro = num_carros_vendidos * valor_fixo_por_carro
    salario_total = salario_fixo + comissao_valor_total + comissao_por_carro
    return round(salario_total, 2)

print(calculo_salario_com_comissao([3, 20000.00, 2000.00, 250.00]))  # Resultado: 3750.00
print(calculo_salario_com_comissao([4, 25000.00, 3500.00, 100.00]))  # Resultado: 5150.00

#5
def calculo_salario(lista):
    tempo_servico, valor_inflacao, salario = lista
    if 1 <= tempo_servico <= 5:
        reajuste_tempo_servico = 0.01
    elif 6 <= tempo_servico <= 10:
        reajuste_tempo_servico = 0.015
    else:
        reajuste_tempo_servico = 0.02
    novo_salario = salario * (1 + reajuste_tempo_servico + (valor_inflacao / 100))
    return round(novo_salario, 2) 

print(calculo_salario([5.1, 6.7, 4500]))  # Resultado: 4869.0
print(calculo_salario([1, 5.7, 4800]))   # Resultado: 5121.6
print(calculo_salario([0, 9.7, 5000]))   # Resultado: 5485.0
print(calculo_salario([10.1, 4.7, 4100]))  # Resultado: 4374.7
print(calculo_salario([1, 5, 2000]))     # Resultado: 2120.0
print(calculo_salario([11, 4.5, 2500]))  # Resultado: 2662.5

#6
def custo_compra(qtd_frutas):
    if qtd_frutas > 10:
        preco_unidade = 1.25
    else:
        preco_unidade = 1.45
    valor_total = qtd_frutas * preco_unidade
    return round(valor_total, 2)

print(custo_compra(2))   # Resultado: 2.90
print(custo_compra(12))  # Resultado: 15.00

#7
def calcula_custos_carro(lista):
    preco_fabrica, custo_distribuidor, impostos = lista
    percentual_distribuidor = (custo_distribuidor / preco_fabrica) * 100
    percentual_impostos = (impostos / preco_fabrica) * 100
    percentual_distribuidor = round(percentual_distribuidor, 2)
    percentual_impostos = round(percentual_impostos, 2)
    return [percentual_distribuidor, percentual_impostos]

print(calcula_custos_carro([100000.00, 12000.00, 20000.00]))  # Resultado: [12.00, 20.00]
print(calcula_custos_carro([115500.00, 25000.00, 32500.00]))  # Resultado: [21.74, 28.26]

#8
def calcula_valor_entrada(lista):
    dia_semana, preco_normal, musica_ao_vivo = lista
    if dia_semana in [1.0, 2.0, 4.0]:
        preco_normal = preco_normal * 0.75
    if musica_ao_vivo == 1.0:
        preco_normal = preco_normal * 1.15
    preco_final = round(preco_normal, 3)
    return preco_final
print(calcula_valor_entrada([3.0, 25.00, 2.0]))  # Resultado: 25.000
print(calcula_valor_entrada([4.0, 50.00, 1.0]))  # Resultado: 43.125
