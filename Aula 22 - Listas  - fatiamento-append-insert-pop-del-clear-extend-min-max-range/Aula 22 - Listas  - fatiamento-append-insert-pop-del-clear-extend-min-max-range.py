"""
Listas em Python
fatiamento
appedn, insert, pop, del, clear, extend, + min, max
appedn:
insert: INSERIR VALOR NA LISTA
pop:
del: DELETA VALOR DA LISTA
clear: LIMPA A LISTA
extend;
+ : JUNTA LISTAS
min:
max:
range:

'''
Variaveis são espaços reservados na memória.

booleanos = True
inteiros = 10
flutuante = 10.0
strings = qwweretet
'''

"""
# jogo de adivinhação usnado listas
secreto = 'perfume'
digitadas = []
while True:
    letra = input('Digite uma letra:  ')
    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)
    #print(digitadas)
    if letra in secreto:
        print(f'UHUUULL, a letra "{letra}" existe na palavra secreta. ')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta. ')
        digitadas.pop()
    #print(digitadas)
# ITERANDO A STRING
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)
    if secreto_temporario == secreto:
        print(f'Acertou mizeraviiii!! a palavra era {secreto_temporario}')
        break


#EXCLUIDO ITENS USANDO O 'DEL'
'''
# INDICES      0 1 2 3 4 5 6 7 8
# INDICES      0 1 2 3 4 5 6 7 8
l2 =          [1, 2, 3, 4, 5, 6, 7, 8, 9]
# INDICES     -9 -8 -7 -6 -5 -4 -3 -2 -1
print(l2)

#del(l2[3])
#print(l2)
del(l2[3:5])
print(l2)
'''
#EXCLUIDO ITENS USANDO O 'MAX' e 'MIN'
'''
l2 =          [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2))
print(min(l2))
'''


# CRIANDO LLISTAS USANDO A FUNÇÃO 'RANGE'
# O RANGE não retorna uma lista, retonar um objeto range
# para tornar um 'RANGE ' em uma lista, é necessário fazer a interação do objeto RANGE usando a função LIST
'''
l2 = list(range(1,10)) # USANDO A FUNÇÃO LIST, O OBJETO RANGE SE TORNA UMA LISTA
#l3 = list(range(1,100,8)) # USANDO A FUNÇÃO LIST, O OBJETO RANGE SE TORNA UMA LISTA ### USANDO MULTIPLOS DE 8
print(l2)
#print(l3)
for valor in l2:
    print(valor)
soma = 0
for valor in l2:
    soma = soma + valor
    print(soma)
'''

# CHECANDO TIPO DO ELEMENTO
'''
l4 = ['String', True, 10, -20.5]
for elem in l4:
    print(f' tipo de elem é {type(elem)} e seu valor é {elem}')
'''

'''
texto ='Valor'
#lista = [1,2,3,4,'Roberto Dias', True, 10.0]
#Indice positivo       0   1   2   3   4   5
lista =              ['A','B','C','D','E',10.5]
lista2 =             ['A','Bacana','C','D','E',10.5]
#Indice negativo      -6    -5     -4  -3  -2  -1
print(lista[-1])
print(lista2[-4])
print(lista[::-1])
string = 'ABCDE' # strings tambem tem indices
print(string[-3:-1])
print(string[::2]) # pulando indices
print(string[::-1]) # pulando indices
'''


## USANDO EXTEND
'''
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2) # juntando listas usando o extend
l2.extend('Roberto') # juntando listas com outros valores usando o extend
#l3 = l1 + l2
print(l1)
print(l2)
#print(l3)
'''
## USANDO APPEND = adiciona valor a lista
'''

l1 = [1,2,3]
l2 = [4,5,6]
l2.append('Roberto')
print(l1)
print(l2)
'''
## USANDO INSERT = adiciona valor em qualquer lugar na lista
'''
l1 = [1,2,3]
l2 = [4,5,6]
l2.insert(0,'Roberto')
l2.insert(1,'Dias')
print(l1)
print(l2)
'''
## USANDO POP = remove valor em qualquer lugar na lista
#l1 = [1,2,3]
'''
l2 = [4,5,6]
print(l2)
l2.insert(0,'Roberto') # adicionaou o valor 'Roberto' no indice 0
print(l2)
l2.pop(0) # removeu o indice 0 da lista
#print(l1)
print(l2)
'''
