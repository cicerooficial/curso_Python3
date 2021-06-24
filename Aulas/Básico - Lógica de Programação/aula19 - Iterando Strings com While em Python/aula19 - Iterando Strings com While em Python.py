#	     Índices
#	     0123456789.......................33
frase = 'o rato roel a roupa do rei de roma'    #Iterável
tamanho_frase = len(frase)
print('Tamanho da frase é: ', tamanho_frase)
contador = 0
nova_string = ''


#Exemplo 1
# while contador < tamanho_frase:
#     print(frase[contador], contador)
#     contador += 1

#Exemplo 2
# while contador < tamanho_frase:
#     nova_string += frase[contador]
#     print(nova_string)
#     contador += 1
#
# print(nova_string)

#Exemplo 3
# while contador < tamanho_frase:
#     letra = frase[contador]
#     if letra == 'r':
#         nova_string += 'R'
#     else:
#         nova_string += letra
#     contador += 1
#
# print(nova_string)


#Exemplo 4

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)