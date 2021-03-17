"""
Entrada de Dados
"""

nome = input('Qual o seu nome? ')
#print(f'O usuário digitou {nome} e o tipo de variável é',type(nome))
idade = input('Qual a sua idade? ')

ano_nascimento = 2021 - int(idade)

print(f'\n{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}.')

# Utilizando TypeCast para formatar o tipo de dado diretamente na entrada
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

print(numero1**numero2)