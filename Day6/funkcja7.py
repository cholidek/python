#zdefiniowanie pomocnicznej funkcji i wkorzytuje ja w 2 funkcji
def odwroc_string(zdanie):
    return zdanie[::-1]

# print(odwroc_string('Nabuchodonozr'))

def odwroc_input():
    zdanie = input('Podaj zdanie: ')
    return odwroc_string(zdanie)

# print(odwroc_input())
