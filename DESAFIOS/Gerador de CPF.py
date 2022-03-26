"""
CPF = 168.995.350-09
_______________________________________
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9 = 60            #    6 * 10 = 60
8 * 8 = 72            #    8 * 9 = 72
9 * 7 = 72            #    9 * 8 = 72
9 * 6 = 63            #    9 * 7 = 63
5 * 5 = 30            #    5 * 6 = 30
3 * 4 = 15            #    3 * 5 = 15
5 * 3 = 15            #    5 * 4 = 20
0 * 2 = 0             #    0 * 3 = 0
                      # -> 0 * 2 = 0
           297        #            343
11 - (297 % 11) = 11  #    11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #    Digito 2 = 9
"""
from random import randint
numero = str(randint(100000000, 999999999))
novo_cpf = numero

reverso = 10
total = 0

# print(novo_cpf)
for index in range(19):
    if index > 8:
        index -= 9
    total += int(novo_cpf[index]) * reverso
# print(cpf[index],index, reverso)


    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)
print(novo_cpf)