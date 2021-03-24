"""
Manipulando strings

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len,abs,type,print, etc ...

Essas funções poder ser usadas diretamente em cada tipo.

Você pode conferir mais informações em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)

"""

# Positivos   [012345678]
texto       = 'Python_s2'
# Negativos  -[987654321]
print(texto[5])

#Exemplo de Fatiamento Positivo
url = 'www.google.com.br/'
print(url[:-1]) #Imprimir sem o último caracter

nova_string = texto[2:6] #O ultimo caracter não é acessível. Sempre +1
print(nova_string)
nova_string = texto[:6] #do inicío até um ponto determinado +1
print(nova_string)
nova_string = texto[7:] #De um ponto até o final
print(nova_string)

#Exemplo de Fatiamento Negativo
nova_string = texto[-1] #Pegando o último numero
print(nova_string)
nova_string = texto[-9:-3] #Pegando o último numero
print(nova_string)

#Exemplo de Fatiamento com Passos de Caracter
nova_string = texto[0:6:2] #Acessando 2 em 2 casas de caracteres
print(nova_string)
nova_string = texto[0::2]
print(nova_string)
