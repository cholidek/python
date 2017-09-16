#  inupt - miesiąc oraz dzien,
#  okreslic pore roku

day = input('Podaj dzień: ')
month = input('Podaj miesiąc bez polskich znaków: ')
day = int(day)

if month == 'kwiecien' or month == 'maj':
    pora_roku = 'wiosna'
if month == 'marzec' and day >= 21:
    pora_roku = 'wiosna'
if month == 'czerwiec' and day <= 21:
    pora_roku = 'wiosna'
if month == 'lipiec' or month == 'sierpien':
    pora_roku = 'lato'
if month == 'wrzesien' and day <= 22:
    pora_roku = 'lato'
if month == 'czerwiec' and day >= 22:
    pora_roku = 'lato'
if month == 'pazdziernik' and month == 'listopad':
    pora_roku = 'jesień'
if month == 'wrzesień' and day >= 23:
    pora_roku = 'jesień'
if month == 'grudzien' and day <= 22:
    pora_roku = 'jesień'
if month == 'styczen' and month == 'luty':
    pora_roku = 'zima'
if month == 'grudzien' and day >= 23:
    pora_roku = 'zima'
if month == 'marzec' and day <= 20:
    pora_roku = 'zima'
print(f'Pora roku to {pora_roku}.')
