"""
 Operação ternária

"""
'''
logged_user = False
#if logged_user:    # MESMO EFEITO DA LINHA DE BAIXO
if logged_user == True:
    msg = 'Usuário Logado. '
else:
    msg = 'Usuário precisa fazer login'
print(msg)



# SOLUÇÃO FACIL USANDO OPERADOR TERNÁRIO
logged_user = False
#msg = 'Usuário Logado. ' if logged_user else 'Usuário precisa fazer login'  # MESMO EFEITO DA LINHA DE BAIXO
msg = 'Usuário Logado. ' if logged_user == True else 'Usuário precisa fazer login'
print(msg)
'''
# OUTRAS SOLUÇÕES USANDO OPERADOR TERNÁRIO
#idade = 18
idade = input("Digite sua Idade: ")
if not idade.isnumeric():
    print('Voce precisa digitar apenas numero inteiro')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode Acessar' if e_de_maior else 'Não pode acessar. '
    print(msg)
'''
if idade >= 18:
    print('Prode acessar.')
else:
    print('não pode acessar')

msg = 'Pode Acessar' if e_de_maior else 'Não pode acessar. '
print(msg)
'''