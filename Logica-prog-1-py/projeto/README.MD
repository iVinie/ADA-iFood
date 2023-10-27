# Projeto de Chatbot para Anotação de Pedidos da Pizzaria Delícia 🍕😋

## Informações de entrega do projeto
- O projeto deve ser realizado em grupo. Os grupos estão separados em arquivos com os nomes dos participantes. Os arquivos podem ser encontrados dentro do Drive Compartilhado da plataforma LMS.
- Informações sobre a entrega:
    - Prazo até o dia 27/10/2023 às 23:59
    - A entrega deverá ser via plataforma LMS, no menu Projeto
    - Formatos aceitos:
        - Códigos python .py ou .ipynb com comentários claros de cada funcionalidade
        - Arquivo .zip com códigos .py ou .ipynb com README.md explicando como executar o código
        - Link do Github com acesso público ou liberado para o professor

## Apresentação do Projeto
Neste projeto, os alunos terão a oportunidade de aplicar conceitos fundamentais de programação em Python, como variáveis, estruturas condicionais, estruturas de repetição, listas e funções, criando um chatbot simples para anotar pedidos de uma pizzaria. Este é um exercício prático e envolvente que permitirá aos alunos desenvolver habilidades essenciais de programação e lógica.

## Descrição do Projeto

Imagine que você está criando um chatbot para a Pizzaria que Delícia, onde o funcionamento da pizzaria é de 17h às 3h da manhã. Os clientes podem fazer pedidos de pizzas disponíveis. O chatbot interagirá com os clientes, perguntando o sabor da pizza desejada e confirmará o preço, caso a pizza escolhida esteja no menu. O chatbot também será capaz de lidar com pedidos de múltiplas pizzas, calcular o valor total do pedido e fornecer uma lista final de pizzas pedidas e o valor total.
<br><br>

---
<br>

## Instruções para os Alunos

### **** DADOS INICIAIS ****

#### *Carregue o menu abaixo em uma lista*
<center>
Menu com pizzas disponíveis:

| Nome da pizza | Preço |
| ------------- | ----- |
| Calabresa     | 70 |
| Queijo        | 50 |
| Pepperoni     | 80 |
| Margherita    | 80 |
| Vegetariana   | 80 |

</center>
<br>

#### *Parâmetro para inciar simular a hora do atendimento*

```python
import random
#horário de funcionamento entre 17 às 03h
hora = random.randint(1,24)
```

### FLUXO PRINCIPAL

#### Atendimento
    - Incie o atendimento ao cliente com uma mensagem de boas vindas.
      - A saudação deverá respeitar a seguinte regra:
          - Quando a hora for menor que 18 - Boa tarde
          - Quando a hora estiver entre 18 e 23 (ambos inclusive) - Boa noite
          - Quando a hora estiver entre 0 e 3 (ambos inclusive) - Bom dia
      - Use o código que está na sessão DADOS INCIAIS para gerar a hora.
    - Após a mensagem de boas vindas apresente o menu de atendimento, que deve ter 2 opções
        - Visualizar Menu
        - Fazer Pedido

#### Visualizar Menu
    - Ao selecionar essa opção o menu deve ser apresentado ao usuário de modo amigável e de fácil leitura
    - A apresentação do menu de vir seguida de uma mensagem perguntando ao usuário se ele já escolheu a pizza, dando duas opções de resposta, sendo uma para iniciar o pedido e outra para sair do chat.

#### Pedidos
    - Inicie o pedido perguntando os dados do cliente
      - Nome do cliente
      - Endereço do cliente
      - Forma de pagamento (Dinheiro, Cartão ou Pix)
    - Em seguida receba o pedido do cliente
    - Verifique se a pizza escolhida está disponível no menu.
        - Caso verdadeiro, confirme o preço da pizza.
        - Caso falso, informe que não está no menu e peça que escolha outra opção
    - Continue perguntando ao cliente se deseja fazer outro pedido.
    - Quando o cliente não quiser fazer mais pedidos, encerre o loop.
    - Ao final do pedido, exiba um resumo com as pizzas pedidas e o valor total do pedido. Use os dados do cliente para ter uma interação maior.
<br><br>

---
<br>

### Conclusão

Este projeto oferece aos alunos a oportunidade de aplicar conceitos fundamentais de programação de uma maneira prática e divertida. Eles podem aprimorar o código, adicionar recursos adicionais, como a opção de bebidas, expandir o menu de pizzas ou integrar o chatbot a um sistema de pedidos em um restaurante real.

### Bônus
As atividades bônus é oferecida apenas para estimular mais o seu desenvolvimento no projeto, não se preocupe caso não consiga entrega-la. O principal é a proposta acima!!

- Em um chatbot a comunicação deve ser o mais humana possível, faça o uso de mensagens para tornar o fluxo fácil de ser entendido, tornando a experiência do usuário objetia e prazerosa.
- Melhore o menu com mais opções e de tamanhos de pizza
- Identifique e comente no final do seu código onde existe a oportunidade de uso de funções
