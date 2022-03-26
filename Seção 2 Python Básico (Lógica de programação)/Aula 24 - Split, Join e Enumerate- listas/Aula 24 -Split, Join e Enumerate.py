"""
Split, Join, Enumerate
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / é usado em objetos iteráveis
"""
'''
string = "O Brasil é o país do futebol, o Brasil é penta."
lista = string.split(' : ')
print(lista)


string2 = "É falso,É falso,É falso, que Brasil foi 'exemplo' na compra de vacinas, como diz Bolsonaro Rayanne Albuquerque Do UOL, em São Paulo 17-01-2022 16h38 É falso que o Brasil foi um 'exemplo para o mundo' na aquisição de vacinas contra a covid-19, como afirmou hoje o presidente Jair Bolsonaro (PL) em entrevista a uma rádio do Espírito Santo. O UOL Confere já havia mostrado, em março do ano passado, que o governo mentia ao dizer que não negligenciou a compra de imunizantes. A gestão federal atrasou a compra de vacinas e, por consequência, a aplicação de doses na população. Fizemos toda nossa parte, inclusive somos um exemplo para o mundo no tocante à aquisição de vacinas. Presidente Jair Bolsonaro e... - Veja mais em "
lista2 = string2.split(',')
#print(lista2)
palavra = ''
contagem = 0

for valor in lista2:
    qtd_vezes = lista2.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

string = "O Brasil é o país do futebol, o Brasil é penta."
lista = string.split(' ')
lista2 = string.split(',')
#print(lista)
for valor in lista2:
    #print(valor.strip()) # STRIP remove o espaço do inicio e do fim da string
     print(valor.strip().capitalize()) # CAPITALIZE  altera o primeiro caracyer para MAIUSULO

'''
'''
# SPLIT
string = "o Brasil é penta."
lista = string.split(' ')
#print(lista)

# JOIN
string2 = '-'.join(lista)
print(string)
print(lista)
print(string2)

# ENUMERATE = retorna tuplas
for v1_indice, v2_valor in enumerate(lista):
    #print(v1_indice, v2_valor.capitalize())
    print(v1_indice,v2_valor,lista[v1_indice])
'''
# LISTA DENTRO ED LISTA
lista = [
    [1,2],
    [3,4],
    [5,6],
]
for v in lista:
    print(v[0])

n1, n2, n3 = lista
print(n2)

