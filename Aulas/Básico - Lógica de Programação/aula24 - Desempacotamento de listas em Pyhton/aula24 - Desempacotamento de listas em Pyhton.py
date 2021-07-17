"""
Desempacotamento de listas em Pyhton
"""

lista = ['Henrique', 'João', 'Maria',1 ,2 ,3 ,4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *_ = lista

print(n1, n2, n3)