#program ktory dzieli zdanie na wyrazy i przydziela je do lsity
#wykorzystanie for
zdanie = 'Ala ma kota i ma cztery łapy'

wyrazy = []

wyraz = ''

for znak in zdanie:
    if znak ==' ':
# ala jak mamy po ali spacje to dodajemy wyraz do listy wyrazy
        wyrazy.append(wyraz)
#ponizsza linijka czysci wyraz zeby sprawdzic nastepne litery
        wyraz =''
        continue
    else:
        wyraz += znak

wyrazy.append(wyraz)
print(wyrazy)

#inny sposób po splicie, przekazujemy po czym bedziemy splitowac
wyrazy2 = zdanie.split(' ')
print(wyrazy2)







# lista jest typem zmiennym, string jest niezmienny - nie mozemy nic wkładać do środka, można podmienić elemnet listy i nie trzeba przypisywać jej do nowej liczby
#i nie przypisywać do tej samej zmiennej
liczby = [0, 1, 2, 4]
liczby.insert(3,3)
print(liczby)

#delete z listy, del mozna usuwac z calej liczby
del liczby[1]
print(liczby)

# #usuwa cala liste i jej nie printuje bo juz nie istnieje w tym miejscu
# del liczby
# print(liczby)

# append - dodaje obiekt na koniec
#extend - dodać całą liczbę do instenijącej listy to mogę rozszerzyć listę


#usuwanie zakresu z listy

del liczby[1:3]
print(liczby)


























