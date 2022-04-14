"""
Criando contador
 count - Itertools
"""
from itertools import count

contador = count()
for valor in contador:
    print(valor)
    if valor >= 10:
        break
print( '#' * 20,'USANDO o START','#' * 20 )
### USANDO o START
contador = count(start=5)
for valor in contador:
    print(valor)
    if valor >= 10:
        break

print( '#' * 20,'USANDO o STEP','#' * 20 )
print('Pula de dois em dois')
### USANDO o STEP
contador = count(start=5, step=2)
for valor in contador:
    print(valor)
    if valor >= 10:
        break

print( '#' * 20,'USANDO o STEP COM ROUND E USANDO PONTO FLUTUANTE','#' * 20 )
contador = count(start=5, step=0.05)
for valor in contador:
    print(round(valor,2))
    if valor >= 10:
        break

print( '#' * 20,'USANDO o STEP CONTAR DE FORM INVERTIDA','#' * 20 )
contador = count(start=0, step=-1)
for valor in contador:
    print(round(valor,2))
    if valor >= 10 or valor <= -10:
        break


print( '#' * 20,'USANDO o CONTADOR NATIVO DO PYTHON','#' * 20 )
contador = count(start=0, step=2)
for cont in  contador:
    if cont <= 10:
      print(cont)

#print(contador)

# cont = 0
# for cont in contador:
#     cont += 1
#     if cont <= 10:
#         print(cont)
