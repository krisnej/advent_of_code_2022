
def check_inclusion_pairs(file_path):
    count = 0
    with open(file_path, 'r') as f:
        for line in f.readlines():
            elf1, elf2 = line.split(',')
            start1, end1 = (int(x) for x in elf1.split('-'))
            start2, end2 = (int(x) for x in elf2.split('-'))
            if start1 <= start2 and end1 >= end2:
                count += 1
            elif start1 >= start2 and end1 <= end2:
                count += 1
            else:
                continue
    return count


if __name__ == '__main__':
    print(check_inclusion_pairs('input.txt'))
