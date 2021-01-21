"""Counting Vowels using a dictionary."""

text = input("Enter a text: ").lower()

vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
}

for letter in text:
    if letter == 'a':
        vowels['a'] += 1
    elif letter == 'e':
        vowels['e'] += 1
    elif letter == 'i':
        vowels['i'] += 1
    elif letter == 'o':
        vowels['o'] += 1
    elif letter == 'u':
        vowels['u'] += 1

print(f'There are ', vowels['a'], '"a"')
print(f'There are ', vowels['e'], '"e"')
print(f'There are ', vowels['i'], '"i"')
print(f'There are ', vowels['o'], '"o"')
print(f'There are ', vowels['u'], '"u"')
