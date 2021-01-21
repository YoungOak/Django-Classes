"""Number Pyramids."""


def pyramid(number):
    """
    Function that make a coefficient's list.
    number: integer

    return: list.
    """
    _list = []
    pyramids_number = number + 1

    for times in range(pyramids_number):
        string = str(times)
        value_list = string * times
        _list.append(value_list)
    inverse = _list[::-1]
    _list.extend(inverse)
    _list.pop(pyramids_number)
    _list.pop(0)
    _list.pop(-1)
    return _list

pyramids_number = int(input('Enter a number to create a pyramid: '))
pyramids_list = pyramid(pyramids_number)
for number in range(len(pyramids_list)):
    print(pyramids_list[number])
