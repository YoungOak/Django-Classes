"""Alphabetical Substring."""


def all_substrings(string):
    """
    Function that gets all the substrings in a row.

    string: string

    return: list
    """
    string = string.lower()
    substrings_list = []
    substrings_list.append(string[0])

    for character in range(len(string)):
        if (
            ord(string[character]) >= 97 and
            ord(string[character]) <= 122
        ):
            if (
                character > 0 and
                (ord(string[character - 1]) == ord(string[character]) - 1) and
                (ord(substrings_list[-1]) != ord(string[character]) - 1)
            ):

                substrings_list.append(string[character - 1])
                substrings_list.append(string[character])
            elif (
                character > 0 and
                (ord(string[character - 1]) == ord(string[character]) - 1)
            ):

                substrings_list.append(string[character])
    if len(substrings_list) < 2:
        substrings_list.append(string[-1])

    return substrings_list


def only_largest(all_substr):
    """
    Function that returns only the largest substring in a list.

    all_substr: list

    return: list

    """
    last_substr = []
    auxiliar = []

    for character in range(len(all_substr)):
        if (character > 0):
            if (
                (ord(all_substr[character - 1]) ==
                 ord(all_substr[character]) - 1)
            ):
                last_substr.append(all_substr[character])
            else:
                if len(last_substr) > len(auxiliar):
                    auxiliar = last_substr[:]
                    last_substr = []
                    last_substr.append(all_substr[character])
                else:
                    last_substr = []
                    last_substr.append(all_substr[character])
        else:
            last_substr.append(all_substr[character])

    if len(auxiliar) > len(last_substr):
        return auxiliar
    else:
        return last_substr


def list_to_str(only_list):
    """
    Function that convert a list in a string.

    only_list: list

    return: string

    """
    for letter in range(len(only_list)):
        if letter == 0:
            largest_str = only_list[letter]
        else:
            largest_str = largest_str + only_list[letter]

    return largest_str

string = input('Enter a string :\n')
if string == '':
    print('You did not enter a string')
else:
    alls = all_substrings(string)
    only = only_largest(alls)
    largest_string = list_to_str(only)
    print(f'The last largest substring on that string is: {largest_string}')
