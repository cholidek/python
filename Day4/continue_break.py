# wypisz liczby z zakresu oprocz podzielnch  podzielne przez 66, cokolwiek bedzie po contninue to nawet jak bedzie print to przechodzi do kolejnego elementu
# i nie drukuje
#
# for i in range(20, 200):
#     if i % 66 == 0:
#         continue
#ta linijka ni bedzie wykonana
#         print('ta licza')
#     print(i)

# for i in range(20, 100):
#     if not i % 66 == 0:
#         print(i)

# jezli napotkam n to przerwij dzialanie petli
# imie = 'Hermenegilda'
#
# for litera in imie:
#     if litera == 'n':
#       break
#     print(litera)
#
# print('Koniec')

#mamy jakis range i chcemy policzyc ile jest liczb parzystych i nieparzystych

# zakres = range(23, 23232)
# il_niepa = 0
# il_pa = 0
#
# for i in zakres:
#     if i % 2 == 0:
#         il_pa += 1
#     else:
#         il_niepa += 1
# print(f'Nieparzyste {il_niepa}, parzyste {il_pa}')

#jezeli mam string policzyc ile jest lister, cyfr, malych liter oraz duzych liter
#wykorzystanie uzycia modulu string


import string

litery = 0
cyfry = 0
male_lit = 0
duze_lit = 0

zdanie = input('Napisz coś:')

for c in zdanie:
    if c.isdigit():
        cyfry += 1
    elif c.isalpha():
        litery += 1
        if c in string.ascii_lowercase:
            male_lit += 1
        else:
            duze_lit += 1

print('Małe litery:', litery)
print('Ilość cyfr:', cyfry)
print('Ilość małych liter:',male_lit)
print('lość dużych liter:', duze_lit)




































