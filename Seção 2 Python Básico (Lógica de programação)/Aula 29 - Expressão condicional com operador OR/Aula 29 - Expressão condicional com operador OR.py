"""
Expressão condicional com operador OR
"""
'''
nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada =(')


# MESMA OPERAÇÃO USANDO O (OR)
# SOLUÇÃO 1

#print(nome or 'Você não digitou nada! ')
# SOLUÇÃO 2
print(nome or None or False or 0 or 'Você não digitou nada! ')

# EXPLICANDO VALORES QUE RETORNA FALSO
'''
a= 0 # retorna falso
b = None  # retorna falso
c = False  # retorna falso
d = []  # retorna falso
e = {}  # retorna falso
f = 22  # retorna verdadeiro
g = 'Luiz' # retorna verdadeiro

variavel = a or b or c  or d or e or f or g
print(variavel)