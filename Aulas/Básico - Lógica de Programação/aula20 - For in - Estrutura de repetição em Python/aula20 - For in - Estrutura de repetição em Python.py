"""
For in em Python
Iterando strings com for
Função range (start=0,stop,step=1)
"""


texto = 'Python'
nova_string = ''
contador = 0

#Exemplo de iteração com while
#

for letra in texto:
    print(letra)

for n, letra in enumerate(texto):
    print(n, letra)

for numero in range(10):
    print(numero)

for numero in range(5, 10):
    print(numero)

for numero in range(0, 10, 1):
    print(numero)

for numero in range(20, 10, -1):
    print(numero)

#Imprimir multiplos
for numero in range(0, 100, 8):
    print(numero)

for numero in range (100):
    if numero % 8 == 0:
        print(numero)

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

#continue - Pula para o próximo laço(iteração)
#break - Para/Sai do laço
for letra in texto:
    if letra == 't':
        continue
        nova_string += letra.upper()
    elif letra == 'h':
        break
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
