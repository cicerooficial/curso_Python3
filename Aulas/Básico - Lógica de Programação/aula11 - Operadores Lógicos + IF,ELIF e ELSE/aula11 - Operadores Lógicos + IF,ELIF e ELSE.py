"""
Operadores Lógicos
and     - E
or      - OU
not     - NÃO
in      - ESTÁ
not in  - NÃO ESTÁ
________________________
_____TABELA VERDADE_____|
X   |   Y   |   X<->Y   |
________________________|
V   |   V   |     V     |
V   |   F   |     F     |
F   |   V   |     F     |
F   |   F   |     F     |
________________________|
"""

#AND - As duas condições precisão ser verdadeiras

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
#Limite para pegar empréstimo
idade_menor = 20 #Muito jovem
idade_maior = 30 # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

#OR  - Uma das duas condições precisão ser verdadeiras
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
#Limite para pegar empréstimo
idade_menor = 20 #Muito jovem
idade_maior = 30 # Passou da idade

if idade >= idade_menor or idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')


#NOT - Inverte o valor da expressão
a = 2
b = 3

if not b > a:
    print('B é maior que A.')
else:
    print('A é maior que B.')
#Usando NOT para verificar se a variável está vazia
A = ''
B = 0
if not A:
    print('Por favor, preencha o valor de A.')
if not B:
    print('Por favor, preencha o valor de B.')

#IN - Verifica se um valor está presente em uma variável
nome = 'Henrique'

if 'q' in nome:
    print(f'Existe a letra q no nome {nome}')

#NOT IN - Verifica se um valor NÃO está presente em uma variável
if 'a' not in nome:
    print(f' Não existe a letra a no nome {nome}')


#Teste de condições

usuario = "admin"
senha = '123456'

nome_usuario = input('Digite o nome do usuário: ')
senha_usuario = input('Digite a senha do usuario: ')

if nome_usuario != usuario and senha_usuario != senha:
    print('Usuário inválido ou senha incorreta.')
else:
    print('Você está logado no sistema!')