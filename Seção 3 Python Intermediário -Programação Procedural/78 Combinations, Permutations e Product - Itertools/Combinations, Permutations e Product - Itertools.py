"""
MODULO ITERTOOLS

Combinations, Permutations e Product - Itertools
Combinação - Ordem não importada
Permutação - Ordem importada
Ambos não repetem valores únicos
Produtos - Ordem importa e repete valores únicos

"""

print('#'*20,'Combinação - Ordem não importada','#'*20)
from itertools import combinations
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia','Fabrício', 'Rose']

for grup in combinations(pessoas, 2):
    print(grup)
print('#'*20,'Combinação - Ordem não importada GRUPO DE 3','#'*20)
from itertools import combinations
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia','Fabrício', 'Rose']

for grup in combinations(pessoas, 3):
    print(grup)

print('#'*20,'Combinação - Ordem  importada','#'*20)
from itertools import permutations
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia','Fabrício', 'Rose']

for grup in permutations(pessoas, 2):
    print(grup)

print('#'*20,'Produtos - Ordem importa e repete valores únicos','#'*20)
from itertools import product
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia','Fabrício', 'Rose']

for grup in product(pessoas, repeat=2):
    print(grup)

print('#'*20,'Ambos não repetem valores únicos','#'*20)