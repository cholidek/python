#  zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

stopnie = input("Podaj stopnie w formacie np '35C' lub '35F: ")
sprawdzenie = stopnie[-1]
stopnie = (stopnie[:-1])
stopnie = int(stopnie)

if sprawdzenie == 'C':
    wyliczenie = stopnie * (9 % 5) + 32
    koncowka = 'F'
else:
    wyliczenie = (stopnie - 32) * (5 % 9)
    koncowka = 'C'

print(f'Temperatura w {koncowka} to {wyliczenie} stopni.')
