# https://adventofcode.com/2025/day/7

def calculate(input_data):
    rows = input_data.split('\n')
    patterns = []
    cols = []
    weight = []
    count = 0
    for i, row in enumerate(rows):
        weight.append([0 for _ in range(len(rows))])
        patterns.append([r for r in row])
        upper_cols = []
        if i != 0:
            upper_cols = list(map(lambda c: c[1], filter(lambda c: c[0] == i - 1, cols)))
        for j, r in enumerate(row):
            upper_weight = weight[i-1][j]
            if r == 'S':
                cols.append([i,j])
                weight[i][j] = 1

            elif r == '^' and j in upper_cols:
                count += 1
                if [i, j - 1] not in cols: cols.append([i,j-1])
                if [i, j + 1] not in cols: cols.append([i, j + 1])

                patterns[i][j-1] = patterns[i][j+1] = '|'

                weight[i][j-1] += upper_weight
                weight[i][j+1] += upper_weight

            elif j in upper_cols:
                if [i,j] not in cols: cols.append([i,j])
                patterns[i][j] = '|'
                weight[i][j] += upper_weight

    for i in range(len(patterns)):
        print(''.join(patterns[i]))

    return count, sum(weight[-1])

file_object = open("input_7.txt", "r")
input_data = file_object.read()

print("Answer:", calculate(input_data))
# part1: 1560
# part2: 25592971184998
