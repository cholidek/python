#sprawdzic czy string jest palindronem, potrojne nacisniecie ' i od razu wstawia i mozna w pomocy ctrl+q i wyswietli w pomocy

from Day6.funkcja7 import odwroc_string

def czy_palindrom(fraza:str):

    '''
    Sprawdza czy podana fraza jest palindromem czyli od
    przodu i na wspak litery sa takie same
    :param fraza:zdanie do sprawdzenia
    :return: zwraca True jestli fraza jest palindronem
    '''

    for litera1, litera2 in zip(fraza, odwroc_string(fraza)):
        if litera1 != litera2:
            return False
        return True

    pass
print(czy_palindrom('kajak'))
print(czy_palindrom('bajka'))

