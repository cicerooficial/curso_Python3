"""
while em Python
Utilizando para realizar ações enquanto uma condição for verdadeira.

Requisitos: Entender condições e operadores

"""
"""
#Exemplo 1
x = 0
while x < 100:
    print(x)
    x += 1

#Exemplo 2
x = 0
while x < 5:
    print(x)
    x += 1

print('Acabou!')

#Exemplo 3
x = 0
while x < 10:
    if x == 3:
        x += 1      #Usa o contador antes da função continue para não ficar em loop infinito
        continue    #Função para pular alguma linha de comando (cuidado com a lógica para não ficar em loop infinito)
    print(x)
    x += 1

#Exemplo 4
x = 0
while x < 10:
    if x == 3:
        x += 1      #Usa o contador antes da função continue para não ficar em loop infinito
        break    #Função para sair do loop while
    print(x)
    x += 1

#Exemplo 5
x = 0 #coluna

while x < 10:
    y = 0 #linha
    while y < 5:
        print(f'{x},{y}')
        y += 1
    x += 1
print('Acabou')
"""

#Exemplo 6


while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    operador = input('Digite um operador: +, -, * ou / ')

    if operador != '+' and operador != '-' and operador != '*' and operador != '/':
        print('Operador não é valido! tente novamente.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)


    # + - * /
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido! Tente novamente.')

    sair = input('Deseja sair? [s] SIM ou [n] NÃO: ')
    if sair == 's':
        print('Obrigado por utilizar a calculadora. Até breve 🖐🏽')
        break