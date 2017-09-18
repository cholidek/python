# sprawdz czy litera jest samogłoska czy spolgloska
# if

dana_litera = input('Wpisz literę: ')


if dana_litera.lower() in ['a', 'e', 'i', 'o', 'y', 'u', 'ą', 'ę']:
    print('Podana przez Ciebie litera jest samogłoską')
else:
    print('Podana przez Ciebie litera jest spółgoską')
