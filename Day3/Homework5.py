#  ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

liczba = input('Podaj liczbę: ')

if liczba.isnumeric():
    liczba = int(liczba)

    if liczba in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
        print('Liczba jest czerwona')
    if liczba in (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35):
            print('Liczba jest czarna')
    if liczba < 18:
        print('Liczba jest wysoka')
    else:
        print('Liczba jest niska')
    if liczba % 2 == 0:
        print('Liczba jest parzysta')
    else:
        print('Liczba jest nieparzysta')


else:
    print('Ale z Ciebie mały rebel, podaj liczbę!')
