from dadosFilter import produtos, pessoas, lista

# print('#'*10, 'USANDO FILTER','#'*10)
# nova_lista= filter(lambda x: x > 5, lista)
# print(list(nova_lista))
#
# print('#'*10, 'USANDO COMPREENSÃO DE LISTAS','#'*10)
# nova_lista2 = [x for x in lista if x > 5]
# print(nova_lista2)

# print('#'*10, 'USANDO FILTER EM UM DICIONÁRIO','#'*0)
# nova_lista3 = filter(lambda p: p['preco'] > 50, produtos)
# for nl3 in nova_lista3:
#      print(nl3)

# print('#'*10, 'USANDO FILTER EM UM DICIONÁRIO- CRIANDO UM FUNÇÃO','#'*0)
#
# def filtra(prduto):
#     if prduto['preco'] > 50:
#         return  True
# nova_lista4 = filter(filtra, produtos)
# for nl4 in nova_lista4:
#      print(nl4)
#
# print('#'*10, 'USANDO FILTER EM UM DICIONÁRIO- CRIANDO UM FUNÇÃO TESTE','#'*0)
# def filtra2(prduto):
#     if prduto['preco'] > 50:
#         prduto[' Está na Promoção!!!'] = True
#     return  True
# nova_lista5 = filter(filtra2, produtos)
# for nl5 in nova_lista5:
#      print(nl5)
# def filtra1(prduto):
#     if prduto['preco'] > 50:
#         return  True
#     else:
#         return False
#
#
# def filtra2(prduto):
#     if not prduto['preco'] > 50:
#         return  False
#     else:
#         return True

print('#'*10, 'USANDO FILTER EM UM DICIONÁRIO- IDADE DA PESSOA','#'*0)
def  filtra(pessoa):
     if pessoa['idade'] < 18:
        return True
nova_lista = filter(filtra, pessoas)

for produto in nova_lista:
    print(produto)