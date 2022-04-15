"""

PARA TRATAR EXCEÇÃO, USA SE o TRY
"""
print('#'* 10, ' Tratando exceção', '#'* 10)
try:
    print(a)
except:
    print('Error')
    pass

print('#'* 10, ' Tratando exceção com NameErro e armazenando em uma variável', '#'* 10)

try:
    a = {}
    print(a[1])

except NameError as erro:
    print('Error de desenvolvimento, fale com o seu desenvolvedor!! \n', erro)

#print('#' * 10, ' Tratando exceção com Exception pega qualquer tipo de erro', '#' * 10)

except (IndexError, KeyError) as erro:
    print('Erro de Indice ou chave. ')
except Exception as erro:
    print('Ocorreu um erro inesperado. \n',erro)
else:
    print('Seu Prgrava entas funcionando')
    pass

### ALEM DO ELSE PODE SER USADO O finally
finally:
    print('finalizando com o finally')

print('\nO programa não vai parar, Segue o Bonde!!')


def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1 / n2
try:
    print(divide(n1=2, n2=0))
except ValueError as error:
    print('Você está tentando dividir por 0. Zero não é divizivel.')
    print('Log ', error)
