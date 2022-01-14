"""
Pass e Ellipsis como placeholders

"""
'''
valor = False
if valor:  # vai dar erro
    # comentario
else:
    print('tchau')
    

#corrigindo usando o pass - usado para reservar o local para escrever codigo futuramente
valor = True
if valor:
    pass
    #comentario
else:
    print('Tchau!!')
'''

#corrigindo usando o ... - usado para reservar o local para escrever codigo futuramente
valor = True
if valor:
    ...
    #comentario
else:
    print('Tchau!!')