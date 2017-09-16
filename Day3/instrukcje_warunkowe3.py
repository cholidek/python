imie = input('Podaj imie:')

print('Witaj', imie)

if imie.isalpha():
    print('Hello', imie)
    if 'a' in imie:
        print("Twoje imie ma literke 'a' ")
    elif 'b' in imie:
        print("Twoje imie ma literke 'b'")
    elif imie == 'Matylda':
        print('Hej Matylda!')
elif imie.isalnum():
    print('Imie musi mieć tylko litery')

if 'a' in imie:
    print("Imię zawiera literę 'a' ")

# jak pierwszy warunek w zagniezdzonym ifie to sprawdza pokolei ale jak pierwszy jest true to reszty nie wchodzi wiec hej matylda sie nie drukuje