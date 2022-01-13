"""
Uma pessoa só pode pegar emprestimo se for maior que 18 anos

"""

#nome_solicitante = input("Nome do solicitante: ")
#idade_solicitante = int(input('Qual sua Idade: '))
"""
#### MINHA SOLUÇÃO

if idade_solicitante >= 18:

    print('Parabéns o emprestimo será liberado' )
else:
    print('Descupe, não fazemos emprestimo para menores de idade')
"""
'''
### SOLUÇÃO DO PROFESSOR
nome = input('Qual o seu nome? ')
idade = (int(input('Qual a sua iadade? ')))
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} NÂO pode pegar o empréstimo. ')
'''
### SOLUÇÃO DO PROFESSOR com ELIF

nome =  'Roberto '#input('Qual o seu nome? ')
idade = (int(input('Qual a sua iadade? ')))
idade_limite = 18

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo. ')

else:
    print(f'{nome} NÂO pode pegar o empréstimo. ')