# Napisz program, który będzie działać jak baza np. studentów
# program ma dać opcje (wyświetlić), po wybraniu którejś, powinien wykonać coś, np:

# 1. baza nowego semestru
# 2. dodaj studenta
# 3. wyszukaj studenta
# 4. usuń studenta
# ...
# x. zakończ program

indeks = 0
def dodaj_studenta(studenci):
    '''
    Funkcja dodająca studenta do listy słowników studenci
    :param studenci:
    :return:
    '''
    global indeks
    indeks += 1
    imie = input('Podaj imię studenta: ')
    nazwisko = input('Podaj nazwisko studenta: ')
    rok_urodzenia = int(input('Podaj rok urodzenia studenta: '))
    srednia_ocen = float(input('Podaj średnią ocen studenta: '))
    student = {'imie': imie, 'nazwisko': nazwisko, 'rok_urodzenia': rok_urodzenia, 'srednia_ocen': srednia_ocen, 'numer_indeksu': indeks}
    studenci.append(student)


def usuwanie_studenta(studenci):
    '''
    Usuwanie studenta po numerze indeksu z listy słowników studenci
    :param studenci:
    :return:
    '''
    numer_indeksu = int(input('Podaj nr indeksu do usunięcia: '))
    for student in studenci:
        if student['numer_indeksu'] == numer_indeksu:
            studenci.remove(student)


def wyszukaj_studenta(studenci):
    '''
    Wyszukuje studenta po nazwisku na liście słowników studenci
    :param studenci:
    :return:
    '''
    nazwisko = input('Podaj nazwisko studenta: ')
    for student in studenci:
        if student['nazwisko'] == nazwisko:
            print(student)

def funkcje_programu():
    '''
    Głowna pętla programu, przyjmuje parametry podane przez użytkownika i je wykonuje
    :return:
    '''
    studenci = []
    while True:
        print('Aby dodać dane studenta wpisz 1.')
        print('Aby usunąć dane studenta wpisz 2.')
        print('Aby wypisać dane studenta wpisz 3.')
        print('Aby zakończyć program wpisz 4.')

        numer = input('Podaj numer: ')

        if numer == '1':
            dodaj_studenta(studenci)

        if numer == '2':
            usuwanie_studenta(studenci)

        if numer == '3':
            wyszukaj_studenta(studenci)

        if numer == '4':
            break

funkcje_programu()
