"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""

numero = input('Digite um numero: ')

if numero.isnumeric():
    numero = int(numero)
    resultado = numero % 2
    if resultado != 0:
        print(f'O numero {numero} é Impar!')
    else:
        print(f'O numero {numero} é Par!')
else:
    print('Não foi informado um número inteiro. Tente novamente!')