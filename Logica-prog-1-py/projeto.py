#Essas linhas importam as bibliotecas random para gerar números aleatórios e tabulate para formatar tabelas.
import random
#No vscode precisa instalar pip install tabulate, biblioteca usada somente para visualização do menu
from tabulate import tabulate

#Estas são listas que representam o menu de pizzas e bebidas, cada uma contendo informações como código, nome e preço dos produtos.
#Lista das pizzas e seus valores
menu_pizza = [
    [1, "Calabresa", 70],
    [2, "Mussarela", 60],
    [3, "Pepperoni", 80],
    [4, "Margherita", 80],
    [5, "Vegetariana", 80],
    [6, "Frango", 80],
    [7, "Quatro Queijos", 85],
    [8, "Portuguesa", 85],
]

#Lista das bebidas e seus valores
menu_bebidas = [
    [9, "Coca-Cola 1L", 8],
    [10, "Pepsi 1L", 7],
    [11, "Guaraná 1L", 7],
    [12, "Fanta 1L", 7],
]

#Lista de sobremesas
menu_sobremesas = [
    [13, "Mousse de Chocolate", 9],
    [14, "Brownie", 7],
    [15, "Fatia de Torta de Brigadeiro", 14 ],
    [16, "Fatia de Torta de Limão", 14],
]

#A variável hora é definida com um valor aleatório entre 1 e 24, simulando a hora do atendimento
hora = random.randint(1, 24)

#A variável taxa_entrega é definida como um valor aleatório entre 7 e 30.
taxa_entrega = random.randint(7, 20)

#A função saudacao é criada para determinar a saudação apropriada com base na hora do atendimento.
def saudacao():
    if hora < 18:
        return "Boa tarde"
    elif 18 <= hora <= 23:
        return "Boa noite"
    else:
        return "Bom dia"

#Três funções, exibir_menu_pizzas, exibir_menu_bebidas e exibir_menu_sobremesas, são definidas para exibir o menu de pizzas, bebidas e sobremesas usando a biblioteca tabulate para formatar a saída em forma de tabela.
#Código para exibir o menu de pizzas usando a biblioteca tabulate
def exibir_menu_pizzas():
    print("Pizzas disponíveis:\n")
    print(tabulate(menu_pizza, headers=["Cod", "Produto", "Preço (R$)"]))
    print("\n")

#Código para exibir o menu de bebidas usando a biblioteca tabulate
def exibir_menu_bebidas():
    print("Opções de refrigerantes:\n")
    print(tabulate(menu_bebidas, headers=["Cod", "Produto", "Preço (R$)"]))
    print("\n")

#Código para exibir o menu de sobremesas usando a biblioteca tabulate
def exibir_menu_sobremesas():
    print("Sobremesas disponíveis:\n")
    print(tabulate(menu_sobremesas, headers=["Cod", "Produto", "Preço (R$)"]))
    print("\n")

#Código principal para simular o atendimento ao cliente
#A função atendimento é a parte principal do programa, onde o atendimento ao cliente é simulado.
def atendimento():
    #Variáveis para armazenar o total do pedido, o pedido em si e uma variável auxiliar produto
    total_pedido = 0
    produto = []
    pedidos = []
    opcao = ""
    #Apresenta opções de atendimento em um loop até que o cliente escolha uma opção.
    while opcao not in ["1", "2"]:
        opcao = input(
            '''
Opções de atendimento:
1. Visualizar menu
2. Fazer pedido
3. Sair
    ''')
        #Se o cliente escolher a opção 1, o menu é exibido. Se escolher a opção 2, o processo de fazer um pedido é iniciado.
        #Código para exibir o menu de pizzas e bebidas
        if opcao == "1":
            exibir_menu_pizzas()
            exibir_menu_bebidas()
            exibir_menu_sobremesas()
            opcao = ""
            continue
        #Código para fazer um pedido
        elif opcao == "2":
            #Solicitado o endereço de entrega e a forma de pagamento
            endereco_cliente = input(f"{nome_cliente}, qual endereço de entrega?: ")
            print('--------------------------------------------------------')
            forma_pagamento = input("Qual a forma de pagamento (Dinheiro|Cartão|Pix)?: ")
            print('--------------------------------------------------------')
            #Verificação da forma de pagamento
            while (forma_pagamento.lower() != "dinheiro") and (forma_pagamento.lower() != "cartão") and (forma_pagamento.lower() != "pix"):
                forma_pagamento = input("Opção invalida! Qual a forma de pagamento (Dinheiro|Cartão|Pix)?: ")
                print('--------------------------------------------------------')
            #Lista para formatar a exibição do pedido no final
            nota_fiscal = [
                ["Cliente", nome_cliente.title()],
                ["Endereço de entrega", endereco_cliente.title()],
                ["Forma de pagamento", forma_pagamento.title()],
            ]
            #While para escolher os produtos, podendo adicionar mais de um
            continuar_pedido = "sim"
            #Exibe o menu novamente
            print("Menu de pizzas, bebidas e sobremesas disponíveis: ")
            exibir_menu_pizzas()
            exibir_menu_bebidas()
            exibir_menu_sobremesas()
            while continuar_pedido.lower() == "sim":
                #Variável que armazena o código do produto que o cliente escolher
                item = input("Digite o código do produto que deseja pedir: ")
                #Faz a verificação se é numérico
                while not item.isdigit():
                    item = input("Código inválido! Digite o código do produto que deseja pedir: ")
                #Se for numérico, passamos para inteiro
                item = int(item)
                #Se o número que o cliente digitou estiver dentro do intervalo da lista das pizzas
                if item in range(1, len(menu_pizza) + 1):
                    #Produto recebe o item escolhido pelo cliente
                    produto = menu_pizza[item - 1]
                    #Adiciona o item à lista de pedidos
                    pedidos.append(produto)
                    #Mostra o produto que foi adicionado
                    print('--------------------------------------------------------')
                    print(f"Pizza de {produto[1]} adicionado com sucesso!")
                #Se o número que o cliente digitou estiver dentro do intervalo da lista das bebidas
                elif item in range(len(menu_pizza) + 1, len(menu_pizza) + len(menu_bebidas) + 1):
                    #Produto recebe o item escolhido pelo cliente
                    produto = menu_bebidas[item - 9]
                    #Adiciona o item à lista de pedidos
                    pedidos.append(produto)
                    #Mostra o produto que foi adicionado
                    print('--------------------------------------------------------')
                    print(f"{produto[1]} adicionado com sucesso!")
                #Se o número que o cliente digitou estiver dentro do intervalo da lista de sobremesas
                elif item in range(len(menu_pizza) + len(menu_bebidas) + 1, len(menu_pizza) + len(menu_bebidas) + len(menu_sobremesas) + 1):
                    #Produto recebe o item escolhido pelo cliente
                    produto = menu_sobremesas[item - 13]
                    #Adiciona o item à lista de pedidos
                    pedidos.append(produto)
                    #Mostra o produto que foi adicionado
                    print('--------------------------------------------------------')
                    print(f"{produto[1]} adicionado com sucesso!")
                #Caso o cliente digitar um número fora do intervalo, pedimos para que ele digite novamente
                else:
                    print("Código inválido!")
                    continue
                #Soma o valor dele no total dos pedidos[]
                total_pedido += produto[2]
                print('--------------------------------------------------------')
                continuar_pedido = input("Deseja fazer mais um pedido? (sim | qualquer tecla para não): ")
                print('--------------------------------------------------------')
        #Caso o cliente desista de pedir
        elif opcao == "3":
            print("Saindo...")
            break
        #Exibe o pedido do cliente, com os dados, itens e valor total
        print("\n          --- Nota Fiscal ---")
        #Variavel auxiliar para criar a exibição dos itens
        itens_pedido = []
        #Adiciona todos os produtos que o cliente escolheu à lista itens_pedidos
        for pedido in pedidos:
            itens_pedido.append([pedido[1], pedido[2]])
        #Exibe os itens adicionado pelo cliente em formato de tabela
        print(tabulate(itens_pedido, headers=["Itens do Pedido", "Valor (R$)"], tablefmt="grid"))
        #Exibe o total do pedido
        print(f"Valor dos produtos: R$ {total_pedido}")
        print(f"Taxa de entrega: R$ {taxa_entrega}")
        print(f"Valor do pedido: R$ {total_pedido + taxa_entrega}")
        print("Obrigado pela preferência!")

#Saudação ao cliente
#faz uma saudação com base na hora e solicita o nome do cliente.
print(f"{saudacao()}, querido cliente! Estou aqui para tornar a sua experiência conosco ainda mais saborosa e conveniente. Na Pizzaria Que Delícia, nosso compromisso é oferecer a você as melhores pizzas, feitas com ingredientes frescos e amor.")
nome_cliente = input(f"Por favor digite o seu nome: ")
print(f"Olá, {nome_cliente.title()}, bem vindo a pizzaria Que Delicia!")
atendimento()
