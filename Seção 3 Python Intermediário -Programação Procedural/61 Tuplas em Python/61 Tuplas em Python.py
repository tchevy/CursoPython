"""
Tuplas em Python, é tipo uma lista onde não se pode mudar os elementos da lista
"""
'''
t1 = (1,2,3, 'A', 'Roberto')
print(t1[4])
print(t1[2:])

for v in t1:
    print(v)


# CONCATENANDO TUPLA
t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)
t3 = t1 + t2
print(t3)


#DESEMPACOTANDO TUPLA EM VARIAVEIS

n1, n2, n3, *_, n10 = t3
print(n3)
print(n10)

# REPETIR O VALOR DA TUPLA USANDO O MUTIPLICADOR
t1 = ('Maria', 'Meiriane', 'Dias', 'de', 'Sousa') * 5
print(t1)
'''
# CONVERTER TUPLA EM LISTA
t1 = (1,2,3,4,5)
t1  = list(t1)
t1[1] = 3000
print(t1)
# CONVERTER PARA TUPLA NOVAMENTE
t1 = tuple(t1)

