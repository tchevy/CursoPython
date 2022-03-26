"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'
nova_string = ''
'''
c = 0
## ITERAÇÂO USANDO O FOR
for letra in texto:
    print(letra)
## USANDO ENUMERATE
for n,letra in enumerate(texto):
    print(n,letra)

## ITERAÇÂO USANDO O WHILE

while c < len(texto):
    print(texto[c])
    c += 1

## USANDO A FUNÇÃO RANGE
for numero in range(10):
    print(numero)
'''
## USANDO O STEP
'''
for numero in range(3,10): # INICIA NO 3 E VAI ATÉ 10
    print(numero)
for numero in range(20,10,-1): # DECREMENTA DE TRAS PARA FRENTE
    print(numero)

## USANDO RANGE
for numero in range(0,100,8): # PULA DE 2 EM 2
    print(numero)

## OUTROS CASOS DE USO

print('*************************')

for numero in range(100):
    if numero % 8 == 0:
       print(numero)
'''
# CONTINUE - pula para o proximo laço
# BREAK - finaliza o liço
for letra in texto:
    if letra == 't':

        nova_string = nova_string + letra.upper()
    elif letra == "h":
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)


