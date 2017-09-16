# operatory logiczne zawierania

s = 'konstantypolitanka'

# operator zawierania in sprawdza czy a sie znajduje w stringu

print('a' in s)
# czy f nie zawiera sie w stringu
print('f' not in s)

# najpierw a in s bedzie sprawdzone pozniej f in s bedzie sprawdzone i prawda i prawda daje prawde
print('a' in s and 'f' not in s)

# type sprawdza typ obiektów
# print(s is type(str))
