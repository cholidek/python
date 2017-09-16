# range nie wyswietli bez petli for zakresu pokaze tylko sam (0,4)
#
# zakres = range(4)
# print(zakres)
#
# for i  in zakres:
#     print(i * 345)


# imie = 'Joanna'
#
# for c in imie:
#     print(c)
# przedział od 30 do 437 co 4 liczba pomnoz *34
# for liczba in range(30, 437, 4):
#     print(liczba * 34)
#
#
# # drukowanie stringa od końca co -1
# wyraz = 'kostantynopolitanka'
#
# for litera in wyraz[::-1]:
#     print(litera.upper())

#
# wyraz = 'konstynopolitanka'

#drukuje tyle printów ile jest w wyrazie
# for litera in wyraz:
#     print('Nie robię nic z lierą')

# dla kazdel litery z imie wypisz ja tyle razy ile wynosi jej indeks

imie = 'Joanna'
# indeks = 0
#
# for litera in imie:
#     print(indeks, litera * (indeks + 1))
#     indeks += 1

# inny sposób na powyże zadanie
# #dostajemy pare wartosci indeks i litera w kazdym przebiegu
# for (indeks, litera) in enumerate(imie):
#     print(indeks, litera * (indeks +1))


#wydrukuje liczbe od 0 do 100 jezeli liczba jest podzielna przez 3 to wypisz Fizz, jeżeli podzielana przez 5 to wypisz Buzz, jeżeli przez 3 i 5 to FizzBuzz
#dzielimy przez 15 bo optymalizacja 3*5
#pozbyć się jednego if fizz i buzz + dodać Homework zoptymalizuj kod
# for i in range(101):
#     if i % 15 ==0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)


# wydrukuj poszzegolne elementy z 2 kolekcje funkcja zip do tego sluży z 2 lub więcej kolekcji będzie brała elemnety z 0 indeksu i pokolei, daje tylko tyle
#elementów ile jest w krótszej kolekcji

kolekcja_a = '0123456789012345'
kolekcja_b = 'Ala ma kota'
#
# for (el_a, el_b) in zip(kolekcja_a, kolekcja_b):
#     print(el_a, el_b)


#sposób na wypisanie bez zipa ale zeby wszystkie znaki z duzszego stringa byly wypisane, zagrozenie ze bedzie indeksowal po krotszym

indeks = 0

for el_a in kolekcja_a:
    print(el_a, kolekcja_b[indeks])
    indeks += 1



















