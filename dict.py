# pentru dictionar se folosesc {}
# country = {'code': 'MD', 'name': 'Alex', 'years': 20}
# country = dict(code="MD", name='Alex', years=20)
# print(country['name'])

# print(country.items())
# for key, value in country.items():
#     print(key, "-", value)

# country = {'code': 'MD', 'name': 'Alex', 'years': 20}
# print(country.get('name'))
# country.clear()
# country.popitem()
# print(country.values())
# country['code'] = 'none'
# print(country.items())

person = {'user1': {
    'fistName': 'John',
    'lastName': 'Kenedy',
    'age': 28,
    'adress': ['Paris 23/1'],
    'hobby': [ 'fotbal', 'voley', 'movie']},
    'user2': {}


}

print(person['user1']['adress'])