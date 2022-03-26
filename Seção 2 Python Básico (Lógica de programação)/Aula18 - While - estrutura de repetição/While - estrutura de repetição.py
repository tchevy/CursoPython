"""
while em Python
utilizado para realizar ações enqunato
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""
'''
print(0)
print(0)
print(0)
print(0)
'''

# USANDO O WHILE
'''
x = 0

while x <= 5:
    print(x)
    x = x + 1

# WHILE COM CONTINUE
while x < 10:
    if  x == 3:
         x = x + 1
         continue

    print(x)
    x = x + 1

print('Acabou!!')
'''
# WHILE COM BREAK


'''
x = 0 # coluna


while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x += 1 # x = x + 1
print('Acabou!!')



while x < 10:
    if  x == 3:
         x = x + 1
         break

    print(x)
    x = x + 1

print('Acabou!!')
'''

## CALCULADORA

while True:
    print()
    num_1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite outro número: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número ou sair [s]im ou [n]ão ')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    ## operadores + - / *

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    sair = input('Deseja Sair? [s]im ou [n]ão ')

    if sair == 's':
        break
    else:
        print('Operador inválido')
