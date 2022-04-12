perguntas = {
    'Pergunta 1': {''
                   'pergunta': 'Quanto é 2 + 2?',
                   'respostas': {
                       'a': '1',
                       'b': '4',
                       'c': '5'},
                   'resposta_certa': 'b',
    },
    'Pergunta 2': {''
                   'pergunta': 'Quanto é 3 * 2?',
                   'respostas': {
                       'a': '4',
                       'b': '10',
                       'c': '6'},
                   'resposta_certa': 'c',
    },
     'Pergunta 3': {''
                   'pergunta': 'Quanto é 2 * 4?',
                   'respostas': {
                       'a': '8',
                       'b': '10',
                       'c': '5'},
                   'resposta_certa': 'a',
    },

}
print()

resposta_certas = 0

for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha a Resposta Certa')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]:{rv}')


    resposta_usuario = input('Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Muito Bem Vc acertou!!!!')
        resposta_certas += 1
    else:
        print('Você errou!!!!')
pqtd_perguntas = len(perguntas)
if resposta_certas >0:
   print(f'Você acertou {resposta_certas}  perguntas.')
else:
   print(f'Você acertou {resposta_certas}  pergunta.')

porcentagem = resposta_certas / pqtd_perguntas * 100
print(f'Você acertou {porcentagem}% das perguntas.')

