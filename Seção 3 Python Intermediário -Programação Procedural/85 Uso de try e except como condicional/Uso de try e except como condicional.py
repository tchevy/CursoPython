print('Digite "Sair" para Fechar o programa!!!')

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:

    numero = converte_numero(input('Digite um número: '))
    if numero is None:
        print('Isso não é numero.')

    else:
        print(numero * 5)






# def converte_numero(valor):
#     try:
#         valor = int(valor)
#         return valor
#     except ValueError:
#         try:
#             valor = float(valor)
#             return valor
#         except ValueError:
#             pass
# while True:
#     numero = converte_numero(input('Digite um número: '))
#     if numero is not None:
#         print(numero * 5)
#     else:
#         print('Isso não é numero.')