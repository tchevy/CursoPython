'''
funçoes que podem ser usadas para definir os tipo da variável
###String Methods###
https://docs.python.org/pt-br/3/library/stdtypes.html
str.isdecimal()
str.isdigit()
str.isnumeric()
str.islower()

'''

# CAUCULADORA

'''
num1 = int(input('Digite um numero'))
num2 = int(input('Digite outro numero'))
#print(num1+num2) # vai dar erro pois todo input é string
print(num1+num2) # agora deu certo, pois converti a string em int
'''
'''
### STRING METHODS ###
num1 = input('Digite um numero')
num2 = input('Digite outro numero')
#print(num1+num2) # vai dar erro pois todo input é string
print(num1.isnumeric())
print(num2.isnumeric())
#print(num1.isnumeric()+num2.isnumeric()) # agora deu certo, pois converti a string em int
'''

num1 = input('Digite um numero')
num2 = input('Digite outro numero')
if num1.isdigit() and num2.isdigit():
    num1=int(num1)
    num2=int(num2)
    print(num1 + num2)
else:
    print('Não foi possivel converter os numeros para realizar contas')
    try: # tenta execultar o codigo caso o codigo anterior não seja valida
        num1 = int(num1)
        num2 = int(num2)
        print(num1 + num2)
    except:
        print('ERROR')