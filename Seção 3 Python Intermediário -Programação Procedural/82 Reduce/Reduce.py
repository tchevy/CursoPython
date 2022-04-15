from ReduceDados import pessoas,produtos,lista
from functools import reduce
acumula = 0
for item in lista:
    acumula += item
print(acumula)

soma_lista= reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos,0 )
print(soma_precos)

print('#' *10, 'Pegar Média de Preços', '#' * 10 )

print(round(soma_precos / len(produtos),2))

print('#' *10, 'Pegar Média de Idade', '#' * 10 )
soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(round(soma_idade/len(pessoas),2))