"""
FORMATAÇÂO DE STRING
"""
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
#print( nome,'tem IMC de :', imc,'kg/m²')
print( nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print( f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome,idade,imc))
print('{2} tem {0} anos de idade e seu imc é {1:.2f}'.format(nome,idade,imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc))


