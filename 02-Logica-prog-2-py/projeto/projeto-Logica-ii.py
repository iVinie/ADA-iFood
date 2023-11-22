import csv
import json
import pandas as pd
from datetime import datetime

def carregar_base_dados():
    caminho_arquivo = fr'C:\Users\vinic\OneDrive\Área de Trabalho\ADA-iFood\ADA-iFood\02-Logica-prog-2-py\projeto\dados.csv'
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        base_dados = list(leitor_csv)
    return base_dados

def obter_assuntos_disponiveis(base_dados):
    return set(tweet.get('subject', '') for tweet in base_dados if tweet.get('subject', ''))

def buscar_por_data(base_dados, data_input):
    try:
        data = datetime.strptime(data_input, "%d/%m/%Y").strftime("%Y-%m-%d")
        
        resultados = [tweet for tweet in base_dados if tweet['date'].startswith(data)]
        exibir_resultados(resultados)
        return resultados
    except ValueError:
        print("Formato de data inválido. Use o formato dd/mm/aaaa.")
        return []

def buscar_por_termo(base_dados, termo):
    resultados = [tweet for tweet in base_dados if termo.lower() in tweet['content'].lower()]
    exibir_resultados(resultados)
    return resultados

def buscar_por_assunto(base_dados, assunto):
    resultados = [tweet for tweet in base_dados if tweet.get('subject', '').lower() == assunto.lower()]
    exibir_resultados(resultados)
    return resultados

def exibir_resultados(resultados):
    if not resultados:
        print("Nenhum resultado encontrado.")
        return

    for tweet in resultados:
        print(f"\nData: {tweet['date']}")
        print(f"Conteúdo: {tweet['content']}")
        print(f"Assunto: {tweet.get('subject', 'N/A')}")

def salvar_resultados(resultados):
    nome_arquivo = input("Digite o nome do arquivo para salvar os resultados (sem a extensão): ")
    nome_arquivo += ".json"
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(resultados, arquivo_json, ensure_ascii=False, indent=2)
    print(f"Resultados salvos em {nome_arquivo}")

def main():
    base_dados = carregar_base_dados()

    while True:
        assuntos_disponiveis = obter_assuntos_disponiveis(base_dados)

        print("\nBoas vindas ao nosso sistema:")
        print("1 - Buscar tweets por data")
        print("2 - Buscar tweets por termo")
        print("3 - Buscar tweets por assunto")
        print("4 - Salvar resultado da busca")
        print("5 - Sair")

        print("Assuntos disponíveis:", assuntos_disponiveis)

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            data = input("Digite a data no formato dd/mm/aaaa: ")
            resultados = buscar_por_data(base_dados, data)
        elif opcao == '2':
            termo = input("Digite o termo que deseja buscar: ")
            resultados = buscar_por_termo(base_dados, termo)
        elif opcao == '3':
            if assuntos_disponiveis:
                print("\nAssuntos disponíveis:")
                for i, assunto in enumerate(assuntos_disponiveis, start=1):
                    print(f"{i}. {assunto}")

                escolha_assunto = input("\nEscolha o número do assunto desejado: ")

                try:
                    escolha_assunto = int(escolha_assunto)
                    if 1 <= escolha_assunto <= len(assuntos_disponiveis):
                        assunto_selecionado = list(assuntos_disponiveis)[escolha_assunto - 1]
                        resultados = buscar_por_assunto(base_dados, assunto_selecionado)
                    else:
                        print("Escolha inválida. Digite um número correspondente a um assunto disponível.")
                        continue
                except ValueError:
                    print("Escolha inválida. Digite um número correspondente a um assunto disponível.")
                    continue
            else:
                print("Nenhum assunto disponível.")
                continue
        elif opcao == '4':
            if 'resultados' in locals():
                salvar_resultados(resultados)
            else:
                print("Nenhum resultado para salvar. Faça uma busca primeiro.")
        elif opcao == '5':
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1-5).")

if __name__ == "__main__":
    main()
