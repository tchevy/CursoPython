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
'''
novo_cpf = '16899535009'

if cpf == novo_cpf:
    print('Válido')
else:    
    print('Inválido')
'''

#cpf = input('Digite seu cpf sem o digito: ')
cpf = 168995350
digito = ''
digito2 = ''

while cpf :
    print(cpf)
    if cpf <= 9:

break