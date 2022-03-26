"""
Entrada de Dados (input)

"""
nome= input("Qual o Seu nome? ")
ano_atual = input("Qual o Ano Atual? ")
ano_nasc = input("Digita o Ano que vc nasceu")
idade = int(ano_atual)-int(ano_nasc)
print()
print(f'{nome} tem {idade} anos.')

nome= input("Qual o Seu nome? ")
idade = input("Qual a sua idade? ")
ano_atual = input("Qual o Ano Atual? ")
ano_nasc = int(ano_atual)-int(idade)
print()
print(f'{nome} tem {idade} anos.')

#nome = input("Qual o seu nome?: ")
print(f'O usuário digitou {nome} e o tipo da varivável é ' f'{type(nome)}')
