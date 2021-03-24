"""
Formatando valores com modificadores

:s  - Texto (strings)
:d  - Inteiros (int)
:f  - Números de ponto flutuante (float)
:;  - (NÚMERO)f - Quantidade de casas decimais (float)
:   - (CARACTER) (> ou < ou ^) (QUATIDADE) (TIPO -s,d ou f)

>   - Esquerda
<   - Direita
^   - Centro
"""
"""
nome = 'Henrique'
print(f'{nome:s}')

valor_1 = 2
valor_2 = 3
soma = valor_1 + valor_2
print(f'{soma:d}')

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:f}')
print('{:.2f}'.format(divisao ))    # Opção1
print(f'{divisao:.2f}')             # Opção2

num_1 = 1
print(f'{num_1:0>10}')  #Esquerda
num_2 = 1150
print(f'{num_2:0<10}')  #Direita
print(f'{num_2:0^10}')  #Centro


nome = 'Henrique'
print(50 - len(nome))
print(f'{nome:#^50}') #Também pode ser com caracteres

"""

#Formatação avançado

nome = 'HenRique'
sobrenome = 'Santos'
#nome_formatado = '{}'.format(nome)
#nome_formatado = '{:@>15}'.format(nome)
#nome_formatado = '{:@>8}'.format(nome)
nome_formatado = '{0:$^50} {1:#^50}'.format(nome,sobrenome)    #Usando com id de variáveis
print(nome_formatado)

#Ourtas funções Strings
print(nome.lower()) #Minúsculo
print(nome.upper()) #MAIÚSCULO
print(nome.title()) #Primeiras Letras Maiúsculas