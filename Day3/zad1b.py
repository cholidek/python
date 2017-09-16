# sprawdz czy liczba jest podzielna przez 3  ,5 ,  7

liczba = input('Podaj liczbę: ')

# sprawdz czy input jest liczba w ifie sprawdzamy czy input nie jest sringiem bo w ifie bedzie wykonany

if liczba.isnumeric():
    liczba = int(liczba)

    if liczba % 3 ==0:
        print(f'Liczba {liczba} jest podzielna przez 3')

    if liczba % 5 ==0:
        print(f'Lidba {liczba} jest podzielna przez 5')

    if liczba % 7 == 0:
        print(f'Liczba {liczba} jest podziela przez 7')
else:
    print(('Podaj mi tylko liczbę!!!'))