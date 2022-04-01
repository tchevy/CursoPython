"""
- Crie uma função1 que recebe uma função2 como parâmetro e
retorne o valor da função executada.


def ola_mundo():
    return 'Olá Mundo!'
def mestre(funcao):
    return funcao()
executar = mestre(ola_mundo)
print(executar)
"""

"""
 2 - Crie uma função 1 que recebe uma função 2 
como parâmetro e retorne o valor da fução2 
executada. Faça a função 1 executar duas funções 
wue recebam um número 
diferente de argumentos.
"""


def mestre(funcao,*args, **kwargs):
    return funcao(*args, **kwargs)
def fala_oi(nome):
    return f'Oi{nome}'
def saudacao(nome, saudacao):
    return f'{saudacao}{nome}'
executando = mestre(fala_oi,' Roberto')
executando2 = mestre(saudacao,' Roberto', saudacao="Bom Dia!!")
print(executando)
print(executando2)

# FUNÇÃO MUTIPLICADOR
def funcao(arg, arg2):
    return arg * arg2
var = funcao(2,2)
print(var)
