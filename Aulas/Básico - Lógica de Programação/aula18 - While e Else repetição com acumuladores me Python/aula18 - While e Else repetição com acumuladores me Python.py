"""
While / Else
Contadores
Acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print(f'Cheguei no else.')

print(f'Isso será executado!')