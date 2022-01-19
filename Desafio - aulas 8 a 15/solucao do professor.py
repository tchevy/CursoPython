"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

#numero_inteiro = input('Digite um número inteiro: ')

#if numero_inteiro.isdigit():
#    pass
#else:
#    print ("Isso não é um número inteiro.")

'''
#### HEAGEM DENTRO DO IF
if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f"{numero_inteiro} é par")
    else:
        print(f" {numero_inteiro} é impar")

else:
    print ("Isso não é um número inteiro.")

'''

'''
### HEAGEM INVERTIDA

if not numero_inteiro.isdigit():
    print('Isso não é um numero inteiro ')

else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
       print(f" {numero_inteiro} é impar ")
    else:
        print(f'{numero_inteiro} é par ')
'''
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. E.
Bom dia 0-11, Boa tarde 12-17 e boa note 18-23

"""

'''
horario = input('Digite um horario (0 - 23): ')
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Horário deve estar entre 0 e 23 ")
    else:
        if horario < 11:
            print('Bom Dia!!')
        elif horario <= 17:
            print('Boa Tarde!! ')
        else:
            print('Boa Noite')
   # pass
else:
    print("Digite um horário entre 0 e 23")
'''
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva " Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

"""

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print(f'Seu nome tem {tamanho} letras, é um nome curto. ')
#elif tamanho >5 and tamanho <8:
 #        print(f'Seu nome tem {tamanho} letras, é um nome normal. ')
elif tamanho <=8:
         print(f'Seu nome tem {tamanho} letras, é um nome normal. ')

else:
        print(f'Seu nome tem {tamanho} letras, é um nome grande. ')

