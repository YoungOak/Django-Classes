"""Utopian tree."""


def calculate_meters(cycles):
    """
    Function that counts the height of a tree.
    cycles: int
    meters: int
    """
    cycles += 1
    meters = 2
    for cycle in range(cycles):
        if cycle == 0:
            meters -= 1
        elif cycle % 2 == 1:
            meters += 2
        else:
            meters += 1

    return meters

trees = int(input('How many trees do you want to test?: '))

for tree in range(trees):
    cycles = int(
        input(
            f'How many cycles for the tree #{tree + 1} do you want to test?: '
            )
                )
    height = calculate_meters(cycles)

    print(f'The tree # {tree + 1} has {height}')
