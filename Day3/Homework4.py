#  oblicz ocenę na podstawie progu procentowego

ocena = input('Podaj wynik testu w zakresie od 0 do 100: ')

if ocena.isnumeric():
    ocena = int(ocena)

    if ocena >= 0 and ocena <30:
            print('Otrzymałęś ocenę 1')

    if ocena >= 31 and ocena <60:
        print ('Otrzymałęś ocenę 2')

    if ocena >= 61 and ocena < 80:
        print('Otrzymałeś ocenę 3')

    if ocena >= 81 and ocena <90:
        print('Otrzymałęś ocenę 4')

    if ocena >= 91 and ocena < 100:
        print("Otrzymałęś ocenę 5")

    if ocena >= 100:
        print('Otrzymałeś ocenę 6')
else:
    print('Ale z Ciebie mały rebel, podaj liczbę!')