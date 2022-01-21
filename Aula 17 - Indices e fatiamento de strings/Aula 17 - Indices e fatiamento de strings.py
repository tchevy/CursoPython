"""

Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""

# indices positivos
#texto = "Hoje é dia de crescimento"
texto = "Python_s2" # cada caractere tem um indice - ex. (P = 0, y = 1 , t = 2, h = 3, o = 4, n = 5)
'''
print(texto[2])

nova_string = texto[2:6] # 2:6 siguinifica que vou pegar o caracter 2 da palavra Python até o caracter 6, assim o resultado será (thon)
nova_string2 = texto[:6] # começa apartir do indice 0 vai ate o indice 5
nova_string3 = texto[7:] # começa apartir do indice 7
print(nova_string)
print(nova_string2)
print(nova_string3)
'''
# indices negativos [-9-8-7-6-5-4-3-2-1]
nova_string4 = texto[-1] # usando o -1 vai ser impresso na tela o caracter 2 da palavra (Python s2), pois está fazendo a checagem de trás para a frente
print(nova_string4)
nova_string5 = texto[-9] # usando o -1 vai ser impresso na tela o caracter P da palavra (Python s2), pois está fazendo a checagem de trás para a frente
print(nova_string5)
nova_string6 = texto[-9:-3] # usando o -1 vai ser impresso na tela oS caracteres Python da palavra (Python s2), pois está fazendo a checagem de trás para a frente
print(nova_string6)

# pulando indices

pula_indice = texto[0:6:2]
print(f'pula indice: {pula_indice}')
pula_indice2 = texto[0::2]
print(f'pula indice2: {pula_indice2}')
pula_indice3 = texto[0::3]
print(f'pula indice3: {pula_indice3}')

# FUNÇÂO (len)

print(len(texto))