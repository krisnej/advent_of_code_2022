their_shape_str = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissor",
}

my_shape_str = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissor",
}

points_their_shapes = {
    "A": 1,
    "B": 2,
    "C": 3,
}

points_my_shapes = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

outcome = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def calculate_outcome_points(their_shape: str, my_shape: str) -> int:
    their = their_shape_str[their_shape]
    my = my_shape_str[my_shape]
    if their == my:
        return 3
    elif their == "Rock" and my == "Scissor":
        return 0
    elif their == "Rock" and my == "Paper":
        return 6
    elif their == "Scissor" and my == "Rock":
        return 6
    elif their == "Scissor" and my == "Paper":
        return 0
    elif their == "Paper" and my == "Rock":
        return 0
    elif their == "Paper" and my == "Scissor":
        return 6
    else:
        raise Exception("Something went wrong calculating the outcome points...")


def part_1(file_path: str) -> int:
    with open(file_path, "r") as f:
        sum = 0
        for line in f.readlines():
            mine = points_my_shapes[line[2]]
            sum += mine
            sum += calculate_outcome_points(line[0], line[2])

        return sum


def choose_shape(theirs: str, outcome: int) -> str:
    if outcome == 3:  # draw
        return theirs
    elif outcome == 0:  # loose
        return {
            "A": "C",
            "B": "A",
            "C": "B",
        }[theirs]
    elif outcome == 6:  # win
        return {
            "A": "B",
            "B": "C",
            "C": "A",
        }[theirs]
    else:
        raise Exception("Invalid outcome.")


def part_2(file_path: str) -> int:
    with open(file_path, "r") as f:
        sum = 0
        for line in f.readlines():
            outcome_points = outcome[line[2]]
            my_shape_letter = choose_shape(line[0], outcome_points)
            my_points = points_their_shapes[my_shape_letter]

            sum += my_points
            sum += outcome_points

        return sum


if __name__ == "__main__":
    print(part_1("input.txt"))
    print(part_2("input.txt"))
