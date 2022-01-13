"""
Operadores Relacionais
== > >= < <= !=

Operador	Nome    	          Função
   ==	   Igual a	        Verifica se um valor é igual ao outro
   !=	   Diferente de     Verifica se um valor é diferente ao outro
   >	   Maior que	    Verifica se um valor é maior que outro
   >=	   Maior ou igual	Verifica se um valor é maior ou igual ao outro
   <	   Menor que	    Verifica se um valor é menor que outro
   <=	   Menor ou igual	Verifica se um valor é menor ou igual ao outro

"""

variavel = 'valor'
print(2 == 2)  # Verdadeiro
#print(2 == 3)  # Falso
print(2  != 3)  # Verdadeiro
print(2 > 3)  # Falso
print(2 >= 3)  # Falso
print(2 < 3)  # Verdadeiro
print(2 <= 3)  # Verdadeiro

num_1 = 2
num_2 = '2'
print(num_1,num_2)
#print(num_1==num_2) # Falso
expressao = num_1 == num_2
print(expressao)
