"""
Tipos de dados
str     - String                | Textos / Cadeia de caracteres
int     - Inteiros              | Números positivos ou negativos ou Zero(sem ponto)
float   - Real/Ponto flutuante  | Números positivos ou ou negativo ou Zero (com ponto)
bool    - Booleano/Lógico       | Confere se os dados são Verdadeiro/Falso (True/False)
"""
print('Nome é um tipo de dado: ',type('Nome'))
print('10 é um tipo de dados: ',type(10))
print('25.23 é um tipo da dado: ',type(25.23))
print('L é igual à l?: ',type('L' == 'l'))
print('L é igual à l?: ',bool('L' == 'l'))
print('10 é igual à 10?: ',bool(10 == 10))

#Valores/ variáveis negativas, não vazias ou zero é dado como não vazio, por isso retorna verdadeiro.
#Se for algum numero negativo ou vazio será negativo.
print('Nome', type('Nome'), bool('Nome'))
print('Nome', type('Nome'), bool(''))

#String: nome
print('Henrique',type('Henrique'))
#Idade: int
print('26',type(26))
#Altura: float
print('1.70',type(1.70))
#É maior de idade 10 > 20
print('10>20',type(10>20))