#sprawdz czy liczba jest podzielna przez 3 i 5 i 7

liczba = input('Podaj liczbę: ')

# sprawdz czy input jest liczba w ifie sprawdzamy czy input nie jest sringiem bo w ifie bedzie wykonany

if liczba.isnumeric():
    liczba = int(liczba)
    if liczba % 3 == 0:
        if liczba % 5 == 0:
            if liczba % 7 == 0:
                print('Liczba jest podzielna przez 3 i 5 i 7')
else:
    print(('Podaj mi tylko liczbę!!!'))