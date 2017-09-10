# dlugosc liczbowa stringa
dlugosc = len('sadajasldjla')
print(dlugosc)



slowo='fsdfdsfsdf'
print(("Słowo {} ma {} liter".format(slowo, dlugosc)))

# od python 3.6 f od format
print(f"slowo {slowo} ma {dlugosc} liter")

# indeksowanie
print(slowo[0])
print(slowo[4])
print(slowo[-3]) #liczy indeksy od drugiej strony czyli od końca stringa [-1] oznacza ostatni element w jakimś zbiorze

#od dlugosc odejmnij -1 i z tej pozycji wstawiawj to samo co print(slowo[-1])
print(slowo[len(slowo) -1])
