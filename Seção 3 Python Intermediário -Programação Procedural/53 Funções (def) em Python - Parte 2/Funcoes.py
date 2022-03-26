'''
#Exemplo 1
def funcao(var):
    return var
variavel = funcao('Valor que Eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum Valor')



#Exemplo 2
def divisao(n1,n2):
        return n1/n2
divide = divisao(8,2)
print(divide)

#Exemplo 03

#ERROR
def divisao(n1, n2):
    return n1 / n2


divide = divisao(8, 0)
print(divide)

#Exemplo 04

def divisao(n1, n2):
    if n2 > 0:
      return n1 / n2


divide = divisao(8, 0)
if divide:
    print(divide)
else:
    print('Conta errada')

#Exemplo 05

def divisao(n1, n2):
    if n2 == 0:
        return
    return  n1 / n2


divide = divisao(8, 1)
if divide:
    print(divide)
else:
    print('Conta inválida')

#Exemplo 06

def dumb():
    return []
var = dumb()
print(var, type(var))
'''
#Exemplo 07
def f(var):
    print(var)
def dumb():
    return f
var = dumb()
print(id(var), id(f))
if var == f:
    print('var é igual a f')
else:
    print('var não é igual a f')