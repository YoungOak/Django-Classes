"""Counting bob's."""


def counting_bobs(text):
    """
    Function that counts the number of bobs in a text.
    text: string

    return: int
    """
    text = text.lower()
    bobs_number = 0
    for letter in range(len(text)):
        if letter >= 2:
            if (text[letter - 2] == 'b' and
                text[letter - 1] == 'o' and
                text[letter] == 'b'
            ):
                # Mau's condition
                # text[char: char+3] = 'bob'
                bobs_number += 1
    return bobs_number

my_text = input('Enter a text: ')
bobs_number = counting_bobs(my_text)
print(f'There are {bobs_number} in the text')
