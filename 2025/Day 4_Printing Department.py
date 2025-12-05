# https://adventofcode.com/2025/day/4

def is_paper(grid, i, j, recursive):
    # position out of grid
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    elif grid[i][j] == '@' or (not recursive and grid[i][j] == 'x'):
        return 1
    else:
        return 0

def remove_paper(input_data, recursive = False):
    rows = input_data.split('\n')
    grid = []
    for row in rows:
        grid.append([i for i in row])

    count = 0
    while True:
        round_count = 0
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                count_papers = (is_paper(grid, i - 1, j - 1, recursive)
                            + is_paper(grid, i - 1, j, recursive)
                            + is_paper(grid, i - 1, j + 1, recursive)
                            + is_paper(grid, i, j - 1, recursive)
                            + is_paper(grid, i, j + 1, recursive)
                            + is_paper(grid, i + 1, j - 1, recursive)
                            + is_paper(grid, i + 1, j, recursive)
                            + is_paper(grid, i + 1, j + 1, recursive))
                if count_papers < 4 and grid[i][j] == '@':
                    round_count += 1
                    grid[i][j] = 'x'

        count += round_count

        for k in range(len(rows)):
            print("".join(grid[k]))

        if not recursive or round_count == 0:
            break

    return count


file_object = open("input_4.txt", "r")
input_data = file_object.read()

# for part 1
print("Answer:", remove_paper(input_data))
# 1491

# for part 2
print("Answer:", remove_paper(input_data, recursive = True))
# 8722