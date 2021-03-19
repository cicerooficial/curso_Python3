"""
DESAFIO 1 - IMC
* Criar variáveis para nome (str), idade(int)
* altura(float) e peso(float) de uma pessoa
* Criar variável com o ano atual(int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves {})
"""

nome            = 'Henrique'
idade           = 26
altura          = 1.70
peso            = 80
ano_atual       = 2021
imc             = peso / altura ** 2
data_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}Kg.\n'
      f'O IMC de {nome} é {imc:.2f}. \n'
      f'{nome} nasceu em {data_nascimento}.')