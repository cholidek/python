#
# def drukuj_kwadrat(x):
#     print(x**2)
#
# drukuj_kwadrat(4)
# ajk przypisze wynik do zmiennej i wypisze to zimenna to zwroci none bo funkcj a nie zwraca

def oblicz_kwadrat(x):
    return x**2

y = oblicz_kwadrat(3)
print(y)

z = y**3
print(z)

print(y%4)

#wywolanie fukcji w innej fukcji
print(oblicz_kwadrat(4))

