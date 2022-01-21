"""
Formatado valores com modificadores - Aula 16

:s - Texto (strings)
:d - Inteiro (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - quantidade de casas decimais (float)
: (ARATERE)(> ou < ou ^ )(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""
num_1 = 1
#num_2 = float(1150)
num_2 = 1150
divisão = num_1/num_2
#print(f'{divisão:.2f}')

#divisão = num_1/num_2
#print('{:.2f}'.format(divisão))

#nome= 'Roberto'
#print(f'{nome}')


print(f'{num_1:0>10}')   # > - Esquerda
#print(f'{num_2:0>10}')
print(f'{num_1:0^10}')   # ^ - Centro
#print(f'{num_2:0^10}')
print(f'{num_1:0<10}')   # < - Direita
#print(f'{num_2:0<10}')


# FLOAT

#print(f'{num_2:0>10}')
print(f'{num_2:.2f}')
print(f'{num_2:0>10.2f}')

## modificando nomes

nome = 'Roberto'
nome2 = 'Roberto Nascimento'
idade = 38
sexo = 'Masculino'
CPF = '007823233'

#nome_formatado = '{:*^50}'.format(nome)
nome_formatado2 = '{n:$^50}'.format(n=nome)
nome_formatado = '{: ^10}{: ^10}{: ^15}{: ^10}'.format(nome,idade,sexo,CPF)
nome_formatado = '{3: ^10}{0: ^10}'.format(nome,idade,sexo,CPF)

print(nome_formatado2)
print(nome_formatado)
print(f'{nome:#^50}')

nome2 = nome2.ljust(30, '$') # usando o metodo .ljust()
print(nome2)
#nome2 = nome2.lower() # usando o metodo .lower()
print(f'CAIXA BAIXA : {nome2.lower()}') # TUDO MINUSCULO
#nome2 = nome2.upper() # usando o metodo .upper()
print(F'CAIXA ALTA : {nome2.upper()}') #TUDO MAIUSCULO
#nome2 = nome2.title() # usando o metodo .title()
print(f'TITULO : {nome2.title()}') # PRIMEIRAS LETRAS MAIUSCULAS