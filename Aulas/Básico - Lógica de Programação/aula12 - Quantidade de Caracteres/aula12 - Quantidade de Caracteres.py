"""
Identificando a quantidade de caracteres com a função len()

Obs.:
1. Não funciona com tipo de dados numéridos (int, float e bool)
2. Espaço também conta
"""

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

#Por trás da função len() ela utiliza o método __len__().
# print(len(qtd_caracteres)) É a mesma coisa que -> print(qtd_caracteres.__len__())

#Teste para checar a quantidade de caracteres
print(usuario,qtd_caracteres,type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres. Tente novamente!')
else:
    print('Você foi cadastrado no sistema!')


string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

#print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')