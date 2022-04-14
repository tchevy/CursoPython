from itertools import groupby, tee

alunos = [
    {'nome': 'Roberto', 'nota': 'A'},
    {'nome': 'Antonio', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'C'},
    {'nome': 'Raimundo', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'C'},
    {'nome': 'Carla', 'nota': 'B'},
    {'nome': 'Camila', 'nota': 'A'},
    {'nome': 'Joana', 'nota': 'B'},
    {'nome': 'Raquel', 'nota': 'A'},
    {'nome': 'Silvia', 'nota': 'B'},
]

# alunos.sort(key=lambda item: item['nota'])
# print('#'*20, 'Ordenando o Dicionário','#'*20)
# for aluno in alunos:
#    print(aluno)
#
# print('#'*20, 'Agrupando o Dicionário','#'*20)
# ordena = lambda item: item['nota']
# alunos.sort(key=ordena)
# alunos_agrupados = groupby(alunos, ordena)
# for agrupamento,valores_agrupados in alunos_agrupados:
#     print(agrupamento)
#     for aluno in valores_agrupados:
#         print(aluno)
#
# print('#'*20, 'Agrupando o Dicionário - OUTRAS MODIFICAÇÕES, USO DO LEN','#'*20)
# ordena = lambda item: item['nota']
# alunos.sort(key=ordena)
# alunos_agrupados = groupby(alunos, ordena)
# for agrupamento,valores_agrupados in alunos_agrupados:
#     print(f'Agrupamento: {agrupamento}\n')
#     for aluno in valores_agrupados:
#         print(len(aluno))

# print('#'*20, 'Agrupando o Dicionário - OUTRAS MODIFICAÇÕES, USO DO LEN , QUANTIDADE DE ALUNO','#'*20)
# ordena = lambda item: item['nota']
# alunos.sort(key=ordena)
# alunos_agrupados = groupby(alunos, ordena)
# for agrupamento,valores_agrupados in alunos_agrupados:
#     print(f'Agrupamento: {agrupamento}\n')
#     quantidade = len(list(valores_agrupados))
#     print(f'{quantidade} alunos tiraram a nota {agrupamento}\n')

print('#'*20, 'Agrupando o Dicionário - OUTRAS MODIFICAÇÕES, USO DO LEN , QUANTIDADE DE ALUNO COM FOR','#'*20)
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
for agrupamento,valores_agrupados in alunos_agrupados:
    va1,novos_valores_agrupados = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}\n')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(novos_valores_agrupados))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}\n')
