"""
TIPOS DE DADOS PRIMITIVOS

str - string  = textos 'Assim'  "Assim"
int - inteiro = 123456 0 -10 -20 -50 -60 15000 1500
float - real/ponto flutuante (negativo ou positivo que tenha ponto) = 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico = (valor logico) = verdadeiro ou falso , True/False  ex. 10==10, sim 10 é igual a 10

"""

# função type (mostra o tipo do dado)
print( type('Roberto'))  # <class 'str'>
print( type(123456))  # <class 'int'>
print( type(False))  # <class 'bool'>
print( type(10.5))  # <class 'float'>


#  Fazendo conversão de tipos tembem chamado de ttype casting
print('10', type('10'), type(int('10')))
# type casting, não funciona para texto
#Ex.
#print('Roberto', (int('Roberto'))) # vai dar erro

# É possivel converter string em float
#Ex.
print('Roberto', (float('38.5')))
print('10' + '10')
print(float('10') * 10)