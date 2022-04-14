# Solução do professor

l1 = '01234567890123456789012345678901234567890123456789'
n = 10
lista = [l1[i:i + n]for i in range(0, len(l1),n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)