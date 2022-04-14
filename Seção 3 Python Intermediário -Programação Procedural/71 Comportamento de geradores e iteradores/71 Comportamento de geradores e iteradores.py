# lists, tuplas, str -> Sequencias -> Iteraveis, tudo que é iteavel pode ser manipulado por for
nome = 'Roberto Nascimento'
for letra in nome:
    print(letra)

print('*' * 100)

nome = 'Francisco'
for letra in nome:
    print(letra)
print('*' * 100)
iterador = iter(nome)
gerador = (letra)
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass