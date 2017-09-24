#zmienne lokalne 'ala', zmienna ola zmienna globalna
imie = 'ola'

def duza_litera(imie='ala'):
    imie = imie.capitalize()
    wiek = 23
    return imie

print(duza_litera())
print(imie)
#zwroci blad bo wiek jest loklany
# print(wiek)