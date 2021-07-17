"""
Operador ternária em Python
"""

logged_user = False

if logged_user:
    mensagem_1 = 'Usuário logado!'
else:
    mensagem_1 = 'Usuário precisa logar!'

print(mensagem_1)

logged_user = False
mensagem_2 = 'Usuario logado!' if (logged_user) else 'Usuário precisa logar!'
print(mensagem_2)



idade = input('Qual a sua idade?: ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    mensagem_3 = 'Pode acessar!' if e_de_maior else 'Não pode acessar!'
    print(mensagem_3)