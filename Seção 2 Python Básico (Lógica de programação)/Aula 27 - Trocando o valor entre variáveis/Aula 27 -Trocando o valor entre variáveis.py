"""
Invertendo valores de variáveis
"""
'''
x = 10 # valor de X é 10
y = 'Luiz' # valor de Y é Luiz

z = x
x = y
y = z
print(f'X={x} e y={y}')
'''
# RESOVENDO DE FORMA FACIL
'''
x = 10 # valor de X é 10
y = 'Luiz' # valor de Y é Luiz
x, y = y, x
print(f'X={x} e y={y}')
'''
# RESOVENDO ADICIONANDO OUTRA VARIÁVEL

x = 10 # valor de X é 10
y = 'Luiz' # valor de Y é Luiz
z = 'Roberto'
x, y, z = z, x, y
print(f'X={x}  y={y} e z={z}')