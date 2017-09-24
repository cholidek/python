# kopiowanie list z typami prostymi

wynik = 3

lista_a = ['zero', 'jeden', wynik]
print('Lista a: ', lista_a)
# 43 sie nie nadpisze bo zostaje 3
wynik = 43
print('lista_a: ', lista_a)


lista_b = lista_a.copy()
print('lista_b: ', lista_b)

#zmiana listy a niepowoduje zmiay listy b
lista_a.append('nowy')
print('lista_a: ', lista_a)
print('lista_b: ', lista_b)

#zwraca nam tozsamosc obiektu
print(hex(id(lista_a)))
print(hex(id(lista_b)))