groceries = {'bananas': 5, 'oranges': 17}
print(groceries['bananas'])
# print(groceries['jabuszko']) #wyjebie blad
print(groceries.get('jabuszko')) #wyjebie none bo nie ma co wziac

ziom = {
    'Pieter': {'phone':'244-223', 'email':'piotro@gmail.com'},
    'Krzychu': {'phone':'223-288', 'email':'krrzychu23@gmail.com'}
}
print(ziom['Pieter'][0])