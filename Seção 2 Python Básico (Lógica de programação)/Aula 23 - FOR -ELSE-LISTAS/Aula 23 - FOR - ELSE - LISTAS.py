"""
For / Else em Python
"""

variavel = ['Roberto', 'Meiriane', 'Cecilia']

'''
for valor in variavel:
    print(valor)
    #continue
    #break
   # print(valor)

for valor in variavel:
    if valor.startswith('M'):
        print('começa com M', valor)
    else:
        print('Não começa com M', valor)
        

comeca_com_C = False
for valor in variavel:
    #if valor.startswith('C'):
    if valor.lower().startswith('C'):
        comeca_com_C = True

if comeca_com_C:
    print(valor,'Começa com C')
else:
    print(valor,'Não começa com C')
'''
# OUTRA FORMA DE RESOLVER O PROBLEMA
for valor in variavel:

    if valor.lower().startswith('m'):
        #print(valor)
        print(valor, 'começa com M')
        #continue

        break


else:
    print('Não existe palavra começando com M.')



