# Índices
# 01234456789...............................33
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
print(tamanho_frase)
contador = 0
nova_string = ''
#print(frase[5])

maiuscula = input('Digite uma Letra para converter para MAIUSCULA: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == maiuscula:
        nova_string += maiuscula.upper()
    else:
        nova_string += letra
    contador += 1
    print(nova_string)


'''
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1


    #print(frase[contador], contador)
   # nova_string += frase[contador]
   # contador += 1
    print(nova_string)
print(nova_string)
'''
