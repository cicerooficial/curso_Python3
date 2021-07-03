"""
FOR / ELSE em Pyhton
"""

variavel = ['Pedro', 'João', 'Maria']

for valor in variavel:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)
#********************************************
comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe um palavra que começa com J.')
#********************************************
comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True
    if valor.lower().startswith('J'):  # lower converte para minúsculo
        print('Existe uma palavra que começa com J.')
        break
else:
    print('Não existe um palavra que começa com J.')
#********************************************
comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True
    if valor.lower().startswith('J'):  # lower converte para minúsculo
        print(valor)
        continue
else:
    print('Não existe um palavra que começa com J.')