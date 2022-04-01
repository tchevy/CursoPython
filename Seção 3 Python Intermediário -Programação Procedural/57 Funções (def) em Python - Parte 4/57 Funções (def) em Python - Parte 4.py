"""
Scopo de variável

Scopo Global
Scopo não global
"""

variavel = 'valor'


def func():
    print(variavel)

def func2():
    variavel = 'valor2'
    print(variavel)
func()
func2()

print(variavel)


