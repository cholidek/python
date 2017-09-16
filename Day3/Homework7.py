# po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu



month = input('Podaj nazwę miesiąca, bez polskich znaków: ')


if month in ('styczen', 'marzec', 'maj', 'lipiec', 'sierpien', 'pazdziernik', 'grudzien'):
  days = '31'
elif month == 'luty':
 days= '28 lub 29'
else:
 days = '30'

print(f'Miesiąc {month} ma {days} dni.')