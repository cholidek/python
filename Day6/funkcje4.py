#argumenty domyslne

def wypisz_imie(imie='lidia'):
    imie = imie.capitalize()
    print(f'Cześć {imie}')

wypisz_imie()
#nadpisuje wargument domyslny przekazany w def
wypisz_imie('janek')

wypisz_imie('ola')

#argument wymagany nie ma podanej wartosci, musi byc podany na poczatku def i sama nazwa argumenty bez wartosci to znaczy ze wymagany, kolejnosc
#najpierw wymagane pozniej domyslne ilosc jest dowolna, mga byc funcje z argumentami domyslnymi i bez , z wymaganymi i bez

#pzyklad na wymagane argumenty (2 pierwsze)
def wypisz_dane(imie, nazwisko, kurs = 'Python', il_dni=15):
    print(imie, nazwisko, kurs, il_dni)

#minimalna ilosc lementow zeby ja wywolac to 2

wypisz_dane('Jan', 'Kowalski')
wypisz_dane('Anna', 'Kowalska', 'Java')
wypisz_dane('Adam', 'Niezgódka', 'malarstwo', 345)
#wydrukuje se na kocu 15 bo kolejnosci jest wazna za python weszlo 30 i na koncu wypisalo 15 z ilosci dni
wypisz_dane('Paulina', 'K', '30')

#trzeba przypisa te 30 do ilosci dni to wtedy nie powstanie powyzszy blad
wypisz_dane('Marek', 'O', il_dni=30)

#zmiana wszystkich argumentow nawet tych wymaganych, mozemy przekazac niepokolei a ona i tak pokazuje pokolei
wypisz_dane(kurs='JavaScript', imie='Ola', il_dni=30, nazwisko='Nowak')


















