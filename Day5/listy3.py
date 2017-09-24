#kolejka - pierwsze przyszło pierwsze wyszło FiFo


kolejka = []

kolejka.append(1)
kolejka.append(56)
kolejka.append(23)

print(kolejka)
#usuwamy za pomoca popa z podaniem indexu
element = kolejka.pop(0)

print(element)
print(kolejka)
kolejka.append(45)
print(kolejka)
kolejka.pop(0)
print(kolejka)

#stos - LiFo

stos= [4324, 432423, 432]

stos.append(87)
stos.append(854)
stos.append(343)
print(stos)
#usunięcie ostatniego elementu z listy
element2 = stos.pop()
print(element2)
print(stos)

