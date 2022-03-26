"""
Desempacotamento de listas
"""
'''
lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista
print(lista[1])
'''
lista2 = ['Luiz', 'João', 'Maria',1,2,3,4,5,6,7,8,9,100]

#n1, n2, n3, *newlist, new1 = lista2  # (new1) está removendo o ultimo item da lista newlist
#print(newlist)
#n1, n2, n3, *newlist = lista2
*newlist, n1, n2, n3 = lista2
#print(n1,n2,n3,newlist)

print(newlist)

