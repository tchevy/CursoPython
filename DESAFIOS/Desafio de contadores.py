"""
for / while

0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
9 1
CRIAR 2 CONTADORES
UM CONTADOR CONTAR DE FORMA PROGRESSIVA E O OUTRO DE MANEIRA REGRESSIVA
"""
contador1  = 0
contador2 = 10

'''
while contador1 <=10:
    #print(contador1)
    contador1 += 1
'''
# MINHA SOLUÇÃO
'''
O laço WHILE é mais usado em solução quando não se sabe se vai ter um fim
'''

print('MINHA SOLUÇÃO')
while contador1 <=8 and contador2 >=0:
    print(contador1, contador2)
    contador1 += 1
    contador2 -= 1

# SOLUÇÃO DO PROFESSOR
'''
Quando a há um limite do laço é indicado usar o FOR
'''
print('SOLUÇÃO DO PROFESSOR')

for p, r in enumerate(range(10, 1 , -1)):
    print(p,r)

