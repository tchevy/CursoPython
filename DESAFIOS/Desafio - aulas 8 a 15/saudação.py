#import datetime
#import time
from _datetime import datetime
#from datetime import timezone
usuario = 'Roberto'

hora = input('Digite o Hora Atual : "  ')
minutos = input('Digite o Minutos: "  ')

#print(datetime.today().strftime('%H:%M'))
#horas = (datetime.today().strftime('%H:%M'))


'''

if horas > 00 <12:
   print(int(f'{horas} Hs'))
   print('Bom dia')

if horas > 12 < 17:
   print(f'{horas} Hs')
   print('Boa Tarde')

if horas > 17 < 24:
   print(f'{horas} Hs')
   print('Boa Noite')
  
'''

#hora = input('Digite Hora atual: ')
#minutos = input('Digite os Minutos: ')
#hora = 12
#minutos = 10

'''
#print(f'{hora}:{minutos}')

if hora >= 00 <11 and minutos > 0 <= 59:
   print('Bom dia')
   print(f'{hora}:{minutos} Hs');
if hora >= 12 <= 18 and minutos > 0 <= 59:
      print('Boa Tarde')
      print(f'{hora}:{minutos} Hs');

'''
if int(hora) <= 12:
    print(f'{hora}:{minutos} Hs')
    print('Bom Dia')
if int(hora) >= 17:
    print(f'{hora}:{minutos} Hs')
    print('Boa Tarde')
if float(hora) > 17 <= 24:
    print(f'{hora}:{minutos} Hs')
    print('Boa Noite')


