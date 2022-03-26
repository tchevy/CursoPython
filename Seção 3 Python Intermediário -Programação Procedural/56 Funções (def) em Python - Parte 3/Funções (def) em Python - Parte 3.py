"""
Funçoes (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""

# #se utilisa a palavra def para defionir uma função e coloca entre parenteses os nomes dos argumentos()
# def func(a1,a2,a3,a4,a5,nome=None, a6=None): # tambem pode ser usado argumento nomeados (usando nome=None não vai dar erro pois o agumento None é nulo)
#     print(a1,a2,a3,a4,a5, nome,a6)
# func(1,2,3,4,5,nome='Roberto',a6=6) # chama a função (vai imprimer os numeros informados)
# var = func(1,2,3,4,5,nome='Roberto',a6=6)
# print(var)

#
# def func(*args): # tupla não pode ser alterada
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
# func(1,2,3,4,5)
#
#
# # FAZER CAST DE TUPLA PARA LIST
#
# def func(*args): # tupla não pode ser alterada
#     args=list(args)
#     args[0] = 20
#     print(args)
#
# func(1,2,3,4,5)
#
# # usado for
#
# def func(*args): # tupla não pode ser alterada
#     for v in args:
#         print(v)
#
# func(1,2,3,4,5)
#
# def func(*args):
#     print(args)
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista,10,20,30,40,50)
# func(*lista,*lista2)


# USANDO **kwargs

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(kwargs['nome'], kwargs['sobrenome'])
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# #func(*lista,10,20,30,40,50)
# func(*lista,*lista2, nome='Roberto', sobrenome='Nascimento')


# fazer checagem de dados
def func(*args, **kwargs):
    print(args)
    #idade = kwargs['idade']
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('idade não existe')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
#func(*lista,10,20,30,40,50)
func(*lista,*lista2, nome='Roberto', sobrenome='Nascimento', idade= 38)