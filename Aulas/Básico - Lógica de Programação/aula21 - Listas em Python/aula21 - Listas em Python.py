"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

texto  = "Valor"

#Modelo de lista
#lista = [1, 2, 3, 4, 'Cícero Henrique', True, 10.5 ]

#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#   -     5    4    3    2    1

string='ABCDE'
print(string[1])
print(lista[1])

#Inserindo novos valores na lista
lista2 = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
lista2[5] = 'Qaulquer outra coisa'

print(lista[0:3])
print(lista[:3])
print(lista[2:])
print(lista[-1]) #Mostra último valor
print(lista[0]) # Mostra primeiro valor
print(lista[::2]) #Omitindo o início e tamanho fixo e declarando somente o tamanho dos pulos/steps
print(lista[::-1])#Inverter uma lista


lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista1)
print(lista2)
print(lista3)

#Funções
lista1.extend(lista2) # função que concatena
lista2.append('b') #Insere um valor no final da lista
lista2.insert(0,'banana') #Insere um valor em uma posição deslocando os demais valores para a direita
lista2.pop() #Deleta o ultimo elemento da lista

#         0,1,2,3,4,5,6,7,8
lista4 = [1,2,3,4,5,6,7,8,9]
print((lista4))
lista4.insert(0,'Banana')
print(lista4)
del(lista4[3:5])
print(lista4)

#Funções MAX e MIN
lista4 = [1,2,3,4,5,6,7,8,9]
print(max(lista4))
print(min(lista4))

lista4 = list(range(1, 10))
print(lista4)

lista4 = list(range(0, 100, 8))
print(lista4)

for valor in lista4:
    print(valor)

lista4 = [1,2,3,4,5,6,7,8,9]
soma = 0
for valor in lista4:
    print(f'{soma} + {valor} = {soma+valor}')
    soma += valor
print(soma)

lista5 = ['String', True, 10, -20.5]

for elem in lista5:
    print(f'O tipo do elemento é {type(elem)} e seu valor é {elem}')


#Jogo descrobrindo a palavra
secreto = 'perfume'
digitadas = []
chances = 3

while True:

    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFFF, a letra "{letra}" NÂO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    #print(secreto_temporario)

    if secreto_temporario == secreto:
        print('Que legal, VOCÊ GANHOU!!!!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances')

