"""
while / else
contadores
acumuladores
"""
contador = 1
acumulador = 1
'''
while contador <= 100:
    print(contador)
    contador += 1
'''
'''
while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
'''
## while mais else
'''
while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Fim')
'''
while contador <= 10:
    print(contador, acumulador)

    if contador > 5:  # usando o BREAK antes do fim do while, o else não será executado
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Fim')
print('Fim fora do laço')
