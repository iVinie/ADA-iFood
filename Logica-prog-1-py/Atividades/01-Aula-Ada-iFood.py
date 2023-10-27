#Atividade 1 Faça um código que mostra a mensagem "Olá mundo" na tela
print('Olá mundo!')

#Atividade 2 Faça um código que peça as 3 notas semestrais e mostre a média simples
nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
nota3 = float(input('Qual a terceira nota: '))

media = (nota1 + nota2 + nota3)/3
print(f'Sua média foi: {media}')

#Atividade 3 Faça um código que peça as 3 notas semestrais e mostre a média ponderada
nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda (vale x2) nota: '))
nota3 = float(input('Qual a terceira (vale x3) nota: '))

media = (nota1 + nota2*2 + nota3*3)/6
print(f'Sua média ponderada foi: {media}')

#Atividade 4 Faça um código que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
salario_hora = float(input('Quanto você recebe por hora: '))
horas = float(input('Quantas horas você trabalhou: '))
print(f'Seu salário foi de {salario_hora * horas}')