"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

'''
if num1.isdigit() and num2.isdigit():
    num1=int(num1)
    num2=int(num2)
    print(num1 + num2)
else:


num_int = (input('Digite um numero inteiro: '))
if num_int.isnumeric():
    print (f'{num_int}')
'''








#usuario = input('Digite seu usuário: ')
usuario = 'Roberto'
num_int = input('Digite um numero inteiro: ')
par = float(num_int) % 2

if par == 0:
    print(f'{usuario} Você digitou um Numero par')
    if num_int.isnumeric():
        print(f'parabéns {usuario} Você digitou o numero {num_int}, esse é um numero inteiro')
#if par != 0:
 #   print(f'{usuario} Você digitou numero impar')
else:
    print(f'{usuario} Você digitou um numero impar')
    print(f'{usuario} Você digitou o numero {num_int}, esse numero não é um inteiro\n')



