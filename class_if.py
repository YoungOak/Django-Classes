# Prueba de IF, ELIF, ELSE

my_number = int(input('Enter a integer number'))

if 5 > my_number:
    print(f'5 is higher than {my_number}')
elif 5 == my_number:
    print(f'{my_number} is 5')
else:
    print(f'5 is lower than {my_number}')
