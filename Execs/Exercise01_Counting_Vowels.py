"""Counting Vowels."""

text = input("Enter a text: ")

count = 0

for letter in text:
    if (
        letter == 'a' or
        letter == 'e' or
        letter == 'i' or
        letter == 'o' or
        letter == 'u' or
        letter == 'A' or
        letter == 'E' or
        letter == 'I' or
        letter == 'O' or
        letter == 'U'):

        count += 1

print(f'There are {count} vowels in the text.')
