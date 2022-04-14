"""
Considerando duas listas de inteiros ou flouats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamamho da menor.

Exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
================== resultado
lista_soma = [2,4,6,8]

# Exemplo
l1 = ['Roberto', 'Nascimento','Dias']
l2 = ['Roberto', 'Nascimento','Roberto', 'Nascimento', 'Dias']
print(l1 != l2)
l1 = set(l1)
l2 = set(l2)
print( l1 == l2)
"""
lista_a = [1,2,3,4,5,6,70,8,9,10]
lista_b = [1,2,3,4,5,6,7,8]
#lista_soma = []
lista_soma = [x +y for x,y in zip(lista_a, lista_b)]
print(lista_soma)


# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)





