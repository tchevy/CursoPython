"""
Variáveis
Iniciar com letras, pode conter números, separar _, letras minúsculas
"""
nome = 'Roberto Dias'
idade = 38 # int
altura = 1.72 # float
e_maior = idade > 18 # bool
peso = 65
#imc = peso/(altura*altura)
imc = peso/altura** 2
print('Nome: ',nome)
print('Idade: ',idade)
print('Altura: ',altura)
print('Peso: ',peso ,'Kg')
print('É maior de Idade?: ',e_maior)
print(nome, 'tem ,', idade , 'anos ,', 'altura de : ', altura,'M,' ' pesa', peso,'Kg')
print( nome,'tem IMC de :', imc,'kg/m²')


