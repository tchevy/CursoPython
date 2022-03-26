"""
* Enumerate - Enumerar elementos da lista # list
"""
lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
]
print(lista[1][2])
enumerada = enumerate(lista)
print(enumerada)
print(list(enumerada))

for v1, v2 in enumerate(lista):
    print(v1,v2)
