# usuń duplikaty z listy

lista = [10, 20, 30, 40, 20, 45, 20, 10, 49, 90, 35, 40]

lista_bez_duplik = []

# jezeli element nie znajduje sie na liscie bez duplikatow to zwieksz lsite bez dulikatow o ten element, w przeciwnym wypadku
#kontynuuj dlej i nic nie rob
for element in lista:
    if element not in lista_bez_duplik:
        lista_bez_duplik.append(element)
    else:
        continue

print(lista_bez_duplik)


