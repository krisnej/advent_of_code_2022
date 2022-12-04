import string


LETTERS = {letter: index for index, letter in enumerate(string.ascii_lowercase+string.ascii_uppercase, start=1)}


def find_duplicate(rucksack: str) -> str:
    first_compartment = rucksack[:int(len(rucksack)/2)]
    second_compartment = rucksack[int(len(rucksack)/2):]
    return ''.join(set([c for c in first_compartment if c in second_compartment]))


def get_priority(duplicate: str) -> int:
    return LETTERS[duplicate]


def find_common_type(file_path: str) -> int:
    sum = 0
    with open(file_path, 'r') as f:
        for line in f.readlines():
            duplicate = find_duplicate(line)
            priority = get_priority(duplicate)
            sum += priority
    return sum


def find_badges(file_path: str) -> int:
    begin_counter = 0
    end_counter = begin_counter+3
    sum = 0
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        for i in range(int(len(lines)/3)):
            next_group = lines[begin_counter:end_counter]
            begin_counter += 3
            end_counter += 3

            badge = ''.join(set([c for c in next_group[0] if c in next_group[1] and c in next_group[2]]))
            priority = get_priority(badge)
            sum += priority
    return sum


if __name__ == '__main__':
    print(find_common_type('input.txt'))
    print(find_badges('input.txt'))



