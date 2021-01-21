# Clase de revisión y captación de Errores con TRY y EXCEPT
import sys


def windows_validation():
    assert ('linux' in sys.platform), "OS Error: This code only run on Windows"
    print('Doing something')

try:
    windows_validation()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as file_error:
        print(file_error)
finally:
    print('This is the finally clause')
