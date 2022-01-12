"""
* Cria variáveis para nome (str), idade (int)
* Altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e  na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
#import  datetime
nome = 'Roberto'
idade = 38
altura = 1.72
peso = (float(65))
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso/altura**2

print('{} Tem  {} Anos de idade\ntem  {:.2f} M de altura, Pesa {:.2f} Kg\n'
      'Nasceu em:  {}, Tem IMC de :  {:.2f} '.format(nome,idade,altura,peso,ano_nasc,imc))
print('Ano Atual:', ano_atual)
print('')
print('')
print('Nome:', (type(nome)))
print('idade:', (type(idade)))
print('altura:', (type(altura)))
print('peso:', (type(peso)))
print('ano_atual:', (type(ano_atual)))
print('ano_nascimento:', (type(ano_nasc)))
print('imc:', (type(imc)))

