num_perg = input("Insira o numero da pergunta: ")
pergunt = input('Insira a pergunta: ')
a = input('Insira o valor para a opção A: ')
b = input('Insira o valor para a opção B: ')
c = input('Insira o valor para a opção C: ')
resp_certa = input('Insira a Resposta: ')

perguntas = {
    f'Pergunta {num_perg}': {''
                   'pergunta': f'{pergunt}?',
                   'respostas': {
                       'a': f'{a}',
                       'b': f'{b}',
                       'c': f'{c}'},
                   'resposta_certa': f'{resp_certa}',

    },
}

with open('dados','a') as dados:
    dados.write(f'{perguntas}')


with open('dados','r') as arquivo:
    pergunta = arquivo.readline()
    print(pergunta[0:])


"""
def peguntar(perguntas):
    return (perguntas)
    
print(perguntas)
"""

