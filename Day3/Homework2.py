# obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

year = input('Podaj rok: ')

if year.isnumeric():
    year = int(year)

    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        print('Podany przez Ciebie rok jest rokiem przestępnym')
    else:
        print("Podany przez Ciebie rok nie jest rokiem przestępnym")
else:
     print('Ale z Ciebie mały rebel, podaj liczbę!')
