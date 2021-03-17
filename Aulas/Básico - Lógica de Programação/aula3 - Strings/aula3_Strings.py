#Pode ser classificado como str = String. São textos dentro de aspas

#Por ter tipagem dinâmica, tudo entre as aspas o interpretador do Python identifica como texto.
print('Isso é um texto')

#Por iniciar com aspas simples, o interpretador fechará o texto ao encontrar outra aspas simples.
#print('Isso é 'um' texto')

#Mas caso o texto precisa ser indicado com aspas, para resolver o problemas acima,
#é só iniciar e fechar o texto com aspas diferente ex: dupla ou tripla.
print("Isso é 'um' texto também com indicação de aspas")

#Caracter de escape, para isolar a quebra de aspas.
# Obs.: Uso não recomendado, para melhor leitura do código
print('Isso é \'um\' texto')

#r no incinio do texto da função print, reconhece tudo como String.
# Obs.: Uso não recomendado, para melhor leitura do código
print(r'Isso é \'um\' texto')
