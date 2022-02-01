secreto = 'python'
secreto_temporario = ''
digitadas = ['o','h','y','p','t','n']

for letra_secreta in secreto:
    print(f'Iteração para a letra{letra_secreta}')
    if letra_secreta in digitadas:
        print(f'Eba, a letra que eu queria é {letra_secreta}')
        secreto_temporario += letra_secreta
    else:
        print(f'Essa letra eu não queria {letra_secreta}')
        secreto_temporario += '*'
print()
print(secreto_temporario)

if secreto == secreto_temporario:
    print('Você ganhou!!')
