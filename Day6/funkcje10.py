
def dodaj_imie(imie, imiona=[]):
    imiona.append(imie.capitalize())
    return imiona
#
# baza = ['Ala']
# #dodanie oli do bazy
# dodaj_imie('Ola', baza)
#
# print(baza)

nowa_baza = dodaj_imie('marta')
print(nowa_baza)


dodaj_imie('marek', nowa_baza)
print(nowa_baza)

# dodal do nowej bazy bo imiona jest zmienna domyslna wiec wszystkie sie dodaja tam, argumenty domyslne waliduje tylko raz python wiec typl zlozony referencyjny

anglicy = dodaj_imie('Tommy')
print(anglicy)

francuzi = dodaj_imie('Pierre')
print(francuzi)

