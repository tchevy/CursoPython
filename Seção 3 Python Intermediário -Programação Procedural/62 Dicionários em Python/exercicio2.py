import copy
clientes = {
    'cliente1':{
        'nome': 'Roberto',
        'Sobrenome': 'Dias',

    },
    'cliente2': {
        'nome': 'Francisco',
        'Sobrenome': 'Nascimento',

    },




}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo{clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
#cliente3 = copy.deepcopy(clientes_v)
#print(cliente3)