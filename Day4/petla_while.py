# while True:
#     print('Hello')

#stan = True
# while stan:
#     print(100)
#     stan = False



# liczba = 1
# while liczba <=100:
#     if liczba % 2 == 0:
#         print(liczba,'Liczba parzysta')
#     else:
#         print(liczba, 'Liczba nieparzysta')
#     liczba += 1


# indeksowanie
#
# imie = 'Joanna'
# indeks = 0
#
# while indeks < len(imie):
#     print(indeks, imie[indeks])
#     indeks += 1

#program sprawdzający hasło, kóre musi mieć minimum 6 znaków i cyfry

# haslo = input('Podaj hasło: ')
# indeks = 0
#
# #sprawdzamy czy mniejsze  bo chemy aby uzytkonik podal 6 znakow i wtedy bedziemy sprawdzac czy znaki, w petli aby do skutku podal 6 znkow
# while not len(haslo) > 6:
#     print('Hasło jest nieprawidłowe!')
#     haslo = input('Podaj hasło: ')
#
# print('Prawidłowe hasło')
#ten program nie dziala bo podmienia prawidlowe na true i dlatego to haslo prawidlowe sie wyswietla pomimo nieprawidlowego
haslo = input('Podaj hasło: ')
prawidlowe = False

while not prawidlowe:
    if len(haslo) < 6:
        prawidlowe = False
        print('Hasło za krótkie!')
    else:
        prawidlowe = True

    if haslo.isalpha():
        print('Hasło musi zawierać cyfry')
        prawidlowe = False
    else:
        prawidlowe = True

    if haslo.isnumeric():
        print('Hasło musi zawierać litery')
        prawidlowe = False
    else:
        prawidlowe =True

    if  prawidlowe:
        haslo = input('Podaj prawidłowe hasło: ')

print('Hasło prawidłowe!')


















