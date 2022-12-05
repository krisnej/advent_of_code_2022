def append_to_stack(stacks: list, s: list, i: int, c: int) -> list:
    # if the last stacks are have less than the maximum number of elements,
    # the rows will be missing whitespaces, and thus throw index errors
    try:
        if stacks[i][c] != ' ':
            s.append(stacks[i][c])
    except IndexError:
        pass
    return s


def parse_stacks(stacks: list):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = ([] for _ in range(9))

    # first element in a list will be the top, last element the bottom of the stack
    for i in range(len(stacks)):
        s1 = append_to_stack(stacks, s1, i, 1)
        s2 = append_to_stack(stacks, s2, i, 5)
        s3 = append_to_stack(stacks, s3, i, 9)
        s4 = append_to_stack(stacks, s4, i, 13)
        s5 = append_to_stack(stacks, s5, i, 17)
        s6 = append_to_stack(stacks, s6, i, 21)
        s7 = append_to_stack(stacks, s7, i, 25)
        s8 = append_to_stack(stacks, s8, i, 29)
        s9 = append_to_stack(stacks, s9, i, 33)

    stacks_list = []
    for stack in s1, s2, s3, s4, s5, s6, s7, s8, s9:
        stacks_list.append(stack)
    return stacks_list


def parse_procedure_line(line: str):
    n = int(line.split()[1])
    from_stack_n = int(line.split()[3])
    to_stack_n = int(line.split()[5])
    return n, from_stack_n, to_stack_n


def move_top(from_stack: list, to_stack: list):
    element = from_stack.pop(0)
    to_stack.insert(0, element)
    return from_stack, to_stack


def move_top_n(n, from_stack: list, to_stack: list):
    move = []
    for i in range(n):
        move.append(from_stack.pop(0))
    move.extend(to_stack)
    return from_stack, move


def part_1(file_path: str) -> str:
    with open(file_path) as f:
        content = f.read().splitlines()
        stacks = content[:8]
        procedure = content[10:]

    stacks_list = parse_stacks(stacks)

    for line in procedure:
        n, from_stack_n, to_stack_n = parse_procedure_line(line)
        for i in range(n):
            stacks_list[from_stack_n-1], stacks_list[to_stack_n-1] = move_top(stacks_list[from_stack_n-1], stacks_list[to_stack_n-1])

    return "".join([stack[0] for stack in stacks_list])


def part_2(file_path: str) -> str:
    with open(file_path) as f:
        content = f.read().splitlines()
        stacks = content[:8]
        procedure = content[10:]

    stacks_list = parse_stacks(stacks)

    for line in procedure:
        n, from_stack_n, to_stack_n = parse_procedure_line(line)
        stacks_list[from_stack_n-1], stacks_list[to_stack_n-1] = move_top_n(n, stacks_list[from_stack_n-1], stacks_list[to_stack_n-1])

    return "".join([stack[0] for stack in stacks_list])


if __name__ == '__main__':
    print(part_1('input.txt'))
    print(part_2('input.txt'))

