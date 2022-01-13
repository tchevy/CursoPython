usuario =input('NOme de Usuário')
senha = input("Senha do usuário")
usuario_bd = 'roberto'
senha_bd = '123456'
if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('usuário ou senha inválida')