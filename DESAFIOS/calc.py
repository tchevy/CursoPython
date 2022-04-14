num1 = range(11)
num2 = input('Digite o Operador: ')
num3 = int(input('Digite o nmero a ser calculado: '))
for num in num1[1:]:
    if num2 == '+':
        print(num ,'+', num3, '=', num + num3)
    elif num2 == '-':
        print(num ,'-', num3, '=', num - num3)
    elif num2 == '/':
        print(num ,'/', num3, '=', num / num3)
    elif num2 == '*':
        print(num ,'X', num3, '=', num * num3)
print('Fim do Calculo !!!!')