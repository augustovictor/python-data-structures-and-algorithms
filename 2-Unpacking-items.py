elements = ['victor', 27, 'rua itapiru', '11 98788-4315', '11 98888-8888']

name, age, address, *phones = elements
*other_attrs, last_phone = elements

print(name)
print(address)
print(phones)
print(last_phone)

#########################

records = [
    ('user', 'victor', 'augusto'),
    ('address', 'rua itapiru', 601, 'saude')
]

def print_user(name, lastname):
    print(f'User: {name} {lastname}')

def print_address(street, number, neighborhood):
    print(f'Address: {street}, {number} - {neighborhood}')

for tag, *args in records:
    if tag is 'user':
        print_user(*args)
    if tag is 'address':
        print_address(*args)

#########################

