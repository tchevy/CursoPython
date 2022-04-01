"""
Dicionário = estrutura de dados que suporta um par de chave e valor

"""
"""
d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'
print(d1['chave1'])

d1 = {}
# OUTRO JEITO DE CHIAR DICONARIO
d1 = dict(chave1 ='Valor da chave', chave2='Valor da outra chave', chave3='valor 3')
#print(d1)

# ADICIONANDO NOVA CHAVE

#d1['nova_chave'] = 'Valor da nova chave'
d1 = { 1:'Valor da chave', 2:'Valor da outra chave', 3:'valor da chave 3' }
print(d1[3])
#print(d1['chave1'])

"""

d1 = {
    'str':'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
}
#print( d1[(1,2,3,4)])
#print(d1[(123)])
#print(d1[('str')])
if 'str' in d1:
    print(d1)
else:
     print('não existe')

print(d1.get('nãoexiste')) # resultado None

if d1.get('nãoexiste') is not None:
    print(d1.get('nãoexiste'))
print(1234)

# UPDATE DE CHAVES
d1.update({'nova_chave':'novo_valor'})
print(d1)

# CHECANDO SE É CHAVE
print('str' in d1)
print('str' in  d1.keys())
print('valor' in d1.values())