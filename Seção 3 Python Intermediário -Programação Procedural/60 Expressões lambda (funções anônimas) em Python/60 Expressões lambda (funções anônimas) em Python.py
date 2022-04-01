" FUNÇÕES LAMBDAS"

def funcao(arg, arg2):
    return arg * arg2
var = funcao(2,2)


# FUNÇÕES LAMBDAS
a =lambda x, y: x *y

print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
#ordenar lista ordem crescente
def func(item):
    return item[1]

lista.sort(key=func)
print(lista)

#ordenar lista ordem decrescente
def func(item):
    return item[1]

lista.sort(key=func, reverse = True)
print(lista)


# EXPRESOES LAMBDAS ordenar lista ordem crescente
lista.sort(key=lambda item: item[1])
print(lista)

# EXPRESOES LAMBDAS ordenar lista ordem decrescente
lista.sort(key=lambda  item: item[1], reverse=True)
print(lista)

# ordenar lista com a função SORTED
print(sorted(lista))

# ordenar lista com a função SORTED

# ordenar  lista com a função SORTED, crescente

print(sorted(lista, key=lambda i:i[1]))

# ordenar  lista com a função SORTED, decrescente
print(sorted(lista, key=lambda i:i[1], reverse=True))

#ORDENAR PELO NOME DO PRODUTO, BASTA MUDAR A CHAVE DE 1 PARA 0
print(sorted(lista, key=lambda i:i[0]))
