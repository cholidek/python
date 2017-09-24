#list comprehension
# w 2 liscie elementy z pierwszej liczby podniesione do kwadratu
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = []

for e in lista:
    lista2.append(e**2)

print(lista2)


lista3 = [x**2 for x in lista]
print(lista3)

# podniesenie listy do potegi 3 ale tylko jezeli lement z listy jest podzielny przez przez 3
lista4 = [x**3 for x in lista if x % 3 ==0]
print(lista4)


zakres_lista = [x**2 for x in range(10)]
print(zakres_lista)
