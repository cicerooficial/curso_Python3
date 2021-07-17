"""
Split, Join, Enumerate em Python
*Split - Dividir uma String # str
*Join - Juntar uma lista #str
*Enumerate - Enumerar elementos da lista #list e objetos iteráveis
"""


string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

for valor in lista_1:
    #print(valor)
    # print(valor) # Sem usar a quebra de linha
    print(f'A palavra {valor} apareceu {lista_1.count(valor)} X na frase.')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista_2:
    print(valor.strip())

# JOIN
string_2 = 'O Brasil é Penta.'
lista_3 = string_2.split(' ')
string_3 = ','.join(lista_3)
print(string_2)
print(lista_3)
print(string_3)

#ENUMERATE
string_2 = 'O Brasil é Penta.'
lista_3 = string_2.split(' ')

for indice, valor in enumerate(lista_3):
    print(indice, valor, lista_3[indice])

lista_4 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for v in lista_4:
    print(v[0], v[1])

lista_5 = [
    [0, 'Henrique'],
    [1, 'João'],
    [2, 'Maria']
]
for indice, nome in lista_5:
    print(indice, nome)

lista_6 = ['Henrique', 'João', 'Maria']

for indice, nome in enumerate(lista_6):
    print(indice, nome)

n1, n2, n3 = lista_6
print(n1, n2, n3)