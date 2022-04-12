# add (adicionar), update (atualizar), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""
# SETs = Conjuntos
s1 = {1,2,3,4,5,6}
# for v in s1:
#     print(v)
#print(s1)

# SET vazio
s2 = set()

# Incrementando valor no SET
s2.add(1)
s2.add(2)
s2.add(3)
s2.add(4)
s2.add((1,2,3,'Roberto'))
#print(s2)

# Removendo valores do SET
s2.discard((1, 2, 3, 'Roberto'))
#print(s2)
s2.update('Estudos')
print(s2)
s2.update([1,2,3,4,5], {6,7,8})
print(s2)
# Atualizando SET (update)

#print(type(s1))

# Unindo STEs, com union ou |
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2
print(s3)

# Interecesão entre os SETs com &
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2
print(s3)

# Pegar a dirença entre SETs

# usando o sinal de - (menos) pega apenas os elementos do set da esquerda
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2
print(s3)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s2 - s1
print(s3)
"""
# symmetric_difference Pega elementos que estão nos 2 SET, porem não estão em ambos
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s2 ^ s1
print(s3)

# Exemplo
l1 = ['Roberto', 'Nascimento','Dias']
l2 = ['Roberto', 'Nascimento','Roberto', 'Nascimento', 'Dias']
print(l1 != l2)
l1 = set(l1)
l2 = set(l2)
print( l1 == l2)

# Fazendo cast

l1 = list(set(l1))
l2 = list(set(l2))
print( l1 , l2)

# Fazendo comparação com o IF

if set(l1) == set(l2):
    print(' L1 é igual a L2 !')
else:
    print('L1 não é igual a L2!!')