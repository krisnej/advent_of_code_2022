def get_elves_calories(input_file: str) -> list[list[int]]:
    """
    return a list with a list of the calories each elf is carrying
    :param input_file: string to input file
    :return: list of lists with separate calories per elf
    [
        [62797],
        [1137, 6086, 6104, 1895, 7909, 1651, 4973, 6964, 5989, 6003, 6859],
        [2817, 3841, 5360, 2614, 1746, 3507, 1159, 3226, 4541, 1007, 3881],
        ...
    ]
    """
    with open(input_file, "r") as input:
        elf: list[int] = []
        elves: list[list[int]] = []

        for line in input.readlines():
            if line != "\n":
                clean_line = int(line.rstrip())
                elf.append(clean_line)
            else:
                elves.append(elf)
                elf = []

        # make sure we didn't have a newline at the end of the file
        # by checking there's one elf left to add
        assert len(elf) > 0
        elves.append(elf)

    return elves


def get_sum_calories(elves: list[list[int]]) -> dict[int, int]:
    """
    Calculate the sum of calories each elf is carrying
    :param elves: list of lists with separate calories per elf
    :return: dictionary with sum of calories per elf
    """
    total_calories: dict[int, int] = {}
    for i, elf in enumerate(elves):
        total_calories[i] = sum(elves[i])

    return total_calories


def get_top_n_elves_calories(total_calories: dict[int, int], n: int) -> int:
    """

    :param total_calories: dictionary with sum of calories per elf
    :param n: number of top results to retrieve
    :return: sum of calories of top n elves
    """
    top_3_elves = sorted(total_calories.values(), reverse=True)[:n]
    return sum(top_3_elves)


if __name__ == "__main__":
    elves = get_elves_calories("input.txt")
    total_calories_per_elf = get_sum_calories(elves)
    top1_elf = get_top_n_elves_calories(total_calories_per_elf, 1)
    top3_elf = get_top_n_elves_calories(total_calories_per_elf, 3)
    print("top 1 elf: ", top1_elf)
    print("top 3 elf: ", top3_elf)
