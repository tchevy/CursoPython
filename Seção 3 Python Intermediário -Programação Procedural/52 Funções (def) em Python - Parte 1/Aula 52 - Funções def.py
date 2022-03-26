"""
Funções - def em Python (Parte 1)


"""
# def saudacao(msg, nome):
#     print(msg, nome)
#
# saudacao('Olá','Roberto')

def saudacao(msg='Olá',nome='Roberto'):
    print(msg, nome)

saudacao()
'''
def saudacao(msg='Olá',nome='Roberto'):
    nome = nome.replace('e','3')
    msg = msg.replace('Olá', 'Tudo bem?')
    print(msg, nome)
saudacao()



def saudacao(msg='Olá',nome='Roberto'):
    print(msg, nome)
saudacao(nome='Zezinho', msg='Hi')
'''