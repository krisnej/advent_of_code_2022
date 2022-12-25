def part_1(file_path):
    with open(file_path) as file:
        content = file.read().splitlines()

    width = len(content[0])
    length = len(content)
    sum = 0

    for l in range(1,length-1):
        for w in range(1, width-1):
            tree = content[l][w]
            above_visible = True
            below_visible = True
            left_visible = True
            right_visible = True

            # look at trees above
            for i in range(1, l+1):
                above = content[l-i][w]
                if above >= tree:
                    above_visible = False
                    break

            # look at trees below
            for i in range(1, length-l):
                below = content[l+i][w]
                if below >= tree:
                    below_visible = False
                    break

            # look at trees left
            for i in range(1, w+1):
                left = content[l][w-i]
                if left >= tree:
                    left_visible = False
                    break

            # look at trees right
            for i in range(1, width-w):
                right = content[l][w+i]
                if right >= tree:
                    right_visible = False
                    break

            any_visible = any([above_visible, below_visible, left_visible, right_visible])
            sum += any_visible

    outside_trees = length+width-1+length-1+width-2

    return sum+outside_trees


def part_2(file_path):
    with open(file_path) as file:
        content = file.read().splitlines()

    width = len(content[0])
    length = len(content)
    max_score = 0

    for l in range(1,length-1):
        for w in range(1, width-1):
            tree = content[l][w]
            above_view = 0
            below_view = 0
            left_view = 0
            right_view = 0

            # look at trees above
            for i in range(1, l+1):
                above = content[l-i][w]
                if above < tree:
                    above_view += 1
                else:
                    above_view += 1
                    break

            # look at trees below
            for i in range(1,length-l):
                below = content[l+i][w]
                if below < tree:
                    below_view += 1
                else:
                    below_view += 1
                    break

            # look at trees left
            for i in range(1, w+1):
                left = content[l][w-i]
                if left < tree:
                    left_view += 1
                else:
                    left_view += 1
                    break

            # look at trees right
            for i in range(1, width-w):
                right = content[l][w+i]
                if right < tree:
                    right_view += 1
                else:
                    right_view += 1
                    break

            score = above_view*below_view*left_view*right_view
            max_score = max(score, max_score)
    return max_score


if __name__ == "__main__":
    print(part_1('input.txt'))
    print(part_2('input.txt'))
