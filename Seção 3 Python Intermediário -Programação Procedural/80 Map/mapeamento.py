from dados import  produtos, pessoas,lista
# # print(lista)
# print('#'*20,'USANDO A FUNÇÃO MAP','#'*20)
#
# nova_lista = map(lambda x: x * 2, lista)
# print(list(nova_lista))
#
#
# print('#'*20,'MESMO RESUTADO USANDO A COMPARAÇÃO DE LISTAS','#'*20)
# nova_lista = [x * 2 for x in lista]
# print(nova_lista)
#
# print('#'*20,'MESMO RESUTADO USANDO DICIONÁRIO','#'*20)
# print(type(produtos))
# for produto in produtos:
#     print(produto)


# print('#' * 20, 'ACRECENTAR 5% EM CADA ITEM DO  DICIONÁRIO', '#' * 20)
# precos = map(lambda p: p['preco'],produtos)
# for preco in precos:
#     print('#' * 20, 'PREÇO NORMAL','#' * 20)
#     print(f'R$ ', preco)
#     print('#' * 20, 'PREÇO COM DESCONTO', '#' * 20)
#     print(f'R$ ', preco - 5*preco/100)

#
# print('#' * 20, 'ACRECENTAR 5% EM CADA ITEM DO  DICIONÁRIO USANDO FUNÇÃO', '#' * 20)
# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05,2)
#     return p
# novos_produtos = map(aumenta_preco,produtos)
# for produto in novos_produtos:
#     print(produto)


# print('#' * 20, 'TRATANDO PESSOAS', '#' * 20)
# for pessoa in pessoas:
#     print(pessoa)
print('#' * 20, 'TRATANDO PESSOAS - CRIAR LISTA SÓ COM OS NOMES', '#' * 20)
nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)

print('#' * 20, 'TRATANDO PESSOAS -  IDADE', '#' * 20)
idade = map(lambda i: i['idade'], pessoas)
for i in  idade:
    print(i)
print('#' * 20, 'TRATANDO PESSOAS - MUDAR IDADE', '#' * 20)
idade = map(lambda i:  i['idade'] * 1.05, pessoas)
for ia in  idade:
    print(int(ia))
print(f'Idade Antiga: ',i,'Nova Idade: ', ia )