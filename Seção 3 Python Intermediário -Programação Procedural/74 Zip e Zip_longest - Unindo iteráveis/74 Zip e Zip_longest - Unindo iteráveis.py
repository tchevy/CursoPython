"""
Zip - Unindo iteraveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
### Código
cidades = ['São Paulo', 'Belo Horizonte', 'salvador', 'Monte Belo']

### Código
estados = ['SP','MG', 'BA']

cidades_estados = zip(cidades,estados)
#print(next(cidades_estados))

#
# for T in cidades_estados:
#     print(T)

# USANDO ZIP_LONGEST
# cidades_estados = zip_longest(cidades,estados)
# for zl in cidades_estados:
#     print(zl)
# print('#' * 80)
# # ADICIONAR ALGUM VALOR ONDE FOR NONE
# cidades_estados = zip_longest(cidades,estados, fillvalue='Estado?')
# for zl in cidades_estados:
#     print(zl)

## USANDO COUNT
cidades_estados = zip(
    indice,
    cidades,
    estados,
)
# for indice,cidades,estados in cidades_estados:
#     print(indice, cidades, estados)

print('#'* 80)

for valor in cidades_estados:
    print(valor)