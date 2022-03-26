# def saudacao(saudacao, nome):
#     print(f'{saudacao} {nome}')
# saudacao('Olá', 'Joãozinho')
# saudacao('Tudo bem?', 'Joãozinho')
# saudacao('Até mais ', 'Joãozinho')
#
# def soma(n1,n2,n3):
#     print(n1+n2+n3)
# soma(2,1,3)
# soma(1,1,1)
# soma(2,1,1)
#
# def aumento_precentual(valor,percentual):
#     print(valor+(valor*percentual/100))
# aumento_precentual(50,10)
# aumento_precentual(100,10)
# aumento_precentual(10,10)
# aumento_precentual(15,100)
# aumento_precentual(2770,10)
#
# def fizbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return 'fizzbuzz'
#     elif n % 5 == 0:
#         return 'buzz'
#     elif n % 3 == 0:
#         return 'fizz'
#     else:
#         return n
# print(fizbuzz(15))
#
#
# # CÓDIGO LIMPO
# def fb(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return  'fizzbuzz'
#     if n % 5 == 0:
#         return 'buzz'
#     if n % 3 == 0:
#         return 'fizz'
#     return n
# print(fb(40))
#
# # USANDO F string
#
# def fb2(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return  f'fizzbuzz, {n} é divisivel por  3 e 5 '
#     if n % 5 == 0:
#         return f'buzz, {n} é divisivel por 5 '
#     if n % 3 == 0:
#         return f'fizz,{n} é divisivel por 3'
#     return n
# print(fb(40))
#
#
def fb3(n):
    if n % 3 == 0 and n % 5 == 0:
        return  f'fizzbuzz, {n} é divisivel por  3 e 5 '
    if n % 5 == 0:
        return f'buzz, {n} é divisivel por 5 '
    if n % 3 == 0:
        return f'fizz,{n} é divisivel por 3'
    return n

# USANDO RANGE
from random import  randint

for i in range(100):
    aleatorio = randint(0,100)
    print(fb3(aleatorio))