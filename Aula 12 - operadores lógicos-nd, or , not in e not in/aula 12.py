"""
Operadores Lógicos
and, or , not
in e not in

and	     Retorna True se ambas as afirmações forem verdadeiras
or	     Retorna True se uma das afirmações for verdadeira
not      retorna Falso se o resultado for verdadeiro
is	     Retorna True se ambas as variáveis são o mesmo objeto
is not	 Retorna True se ambas as variáveis não forem o mesmo objeto

"""

a = 2
b = 2
c = 3
result = a == b and b < c
result2 = a == b or b < c
result3 = not a == b and not b < c
result4 = a == b is b < c
result5 = a == b is not b < c
print(result)
print(result2)
print(result3)
print(result4)
print(result5)

#Ex.
#  Verdadeiro e verdadeiro = verdadeiro
#  Verdadeiro e False = falso
#  caparacao1 and comparacao2
#

nome = 'Roberto Dias'
if 'Dia' not in nome:
    print("Executei.")
else:
    print("Existe o texto.")