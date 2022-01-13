'''
#nome = input('Digite seu Usuário')
nome = ('roberto')
senha = input(' Digite sua senha: ')
qtd_caracteres = len(senha)

if qtd_caracteres >= 8:
    print(f"Ok , {nome} Você está logado ")
else:
    print("a senha não poder ter menos de 8 caracteres")

 #   print(nome, qtd_caracteres,type(qtd_caracteres))
'''
# Usar 2 strings e somar a quantidade de caracteres
string1 = input('Digite string1')
string2 = input('Digite string2')
qtd_total = len(string1 + string2)
#print(f'A quantidade total de caracteres digitados foi {len(string1)} + {len(string2)}')
print(f'A quantidade total de caracteres digitados foi {qtd_total}')
print(string2.__len__())