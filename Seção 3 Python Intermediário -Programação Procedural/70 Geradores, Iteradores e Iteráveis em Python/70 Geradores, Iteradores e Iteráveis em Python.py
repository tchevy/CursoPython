"""
  Iteraveis
  Ex. [0,,1,2,3,4,5]

  Iteradores
  geradores

"""
#lista = [0, 1, 2, 3, 4, 5]
#print(hasattr(lista, '__iter__'))

# checando se lista é um iterador
#print(hasattr(lista, '__next__'))  # False, lsita não é interador

# Quando o objeto é iteravel, pode se usaro o for para manipular o objeto
# Ex.
# for v in lista:
#     print(v)

# checando se lista é um iterador
'''
lista = iter(lista)
print(hasattr(lista, '__next__'))  # True, lista  é interador
print(next(lista))  # usando iterador, o printe imprime o conteudo sequencialmente uma por vez
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
# quando se usar o for, o objeto(lista) passa a ser um iterador
'''
import sys
import time
#  geradores
# lista2 = list(range(10))
# print(sys.getsizeof(lista2))

def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel
g = gera()
print(next(g))
print(next(g))
print(next(g))

# LISTA
lista = [x for x in range(1000)]
print(type(lista))
print(f'USO DE MEMORIA LISTA',sys.getsizeof(lista),'Bytes')

# GERADOR
lista = (x for x in range(1000))
print(type(lista))
print(f'USO DE MEMORIA GERADOR',sys.getsizeof(lista),'Bytes')


# ver quanto de memoria o objeto esta consumindo
print('******************************************')
print(sys.getsizeof(gera))
