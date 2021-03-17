"""
Operadores Relacionais

==  - Igual a
>   - Maior que
<   - Menor que
>=  - Maior que igual a
<=  - Menor que igual a
!=  - Diferente
"""
"""
EXEMPLOS:

num_1   = 3 #int
num_2   = 2 #int

expressao = num_1 == num_2
print(expressao)

expressao = num_1 > num_2
print(expressao)

expressao = num_1 < num_2
print(expressao)

expressao = num_1 >= num_2
print(expressao)

expressao = num_1 <= num_2
print(expressao)

expressao = num_1 != num_2
print(expressao)
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
#Limite para pegar empréstimo
idade_menor = 20 #Muito jovem
idade_maior = 30 # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')