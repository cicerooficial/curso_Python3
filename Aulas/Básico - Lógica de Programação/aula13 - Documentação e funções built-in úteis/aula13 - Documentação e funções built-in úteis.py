"""
Documentação e funções built-in úteis
Link: https://docs.python.org/3/library/stdtypes.html#:~:text=Numeric%20Types%20%E2%80%94%20int%20%2C%20float%20%2C,Integers%20have%20unlimited%20precision.

# Funções de verificação de entrada de valores Strings
#isnumeric  - Verifica se o valor é um número inteiro e se é positivo
#isdigit    - Verifica se o valor é um caracter e se é positivo
#isdecimal  - Verifica se o valor é um número decimal e se é positivo

# Deixando a verificação separado evitamos de entrar em um erro logo de cara, caso o usuário digite um valor fora do esperado.
"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

#isnumeric - Exemplo de teste
#print(num1.isnumeric())
#print(num2.isnumeric())

#isdigit - Exemplo de teste
#print(num1.isdigit())
#print(num2.isdigit())

#isdecimal - Exemplo de teste
#print(num1.isdecimal())
#print(num2.isdecimal())

'''
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não foi possível converter os números para realizar contas.')
'''

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print('ERROR')
