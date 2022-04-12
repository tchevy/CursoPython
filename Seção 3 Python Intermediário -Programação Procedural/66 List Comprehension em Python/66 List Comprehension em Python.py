"""
List Comprehension = Compreenções de listas
"""

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1] # mutiplica v por 2

ex3 = [(v,v2) for v in l1 for v2 in range(3)]

l2 = ['Meiriane', 'Roberto', 'Filho']
ex4 = [v.replace('a','@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(x,y) for x, y in tupla]
ex5 = dict(ex5)

#print(ex1)
print(ex2)
# print(ex3)
# print(ex4)
#print(ex5['chave2'])

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0] # Numeros divisiveis por 2
#print(ex6)

ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0] # Numeros divisiveis por 3 e por 8 diolinux

#print(ex7)

# usando else

ex8 = [v if v % 3 == 0 else '#' for v in l3] # Numeros divisiveis por 2
#print(ex8)

ex9 =  [v if v % 3 == 0 and v % 8 ==0 else '#' for v in l3] # Numeros divisiveis por 3 e 8 usando and e else
print(ex9)