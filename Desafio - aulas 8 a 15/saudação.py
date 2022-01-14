usuario = 'Roberto'
horas = str(input('Digite o Horario Atual "perando hora dos minutos por " : "  '))

if horas.format(float) > 00 <12:
   print(f'{horas} Hs')
   print('Bom dia')

if horas > 12 < 17:
   print(f'{float(horas)} Hs')
   print('Boa Tarde')

if horas > 17 < 24:
   print(f'{float(horas)} Hs')
   print('Boa Noite')
