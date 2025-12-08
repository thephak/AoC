# https://adventofcode.com/2025/day/8
import math

def join_circuit(new_group: list[int], current_groups: list[list[int]]):
    merged_group = []
    remaining_groups = []

    for group in current_groups:
        # Get all current groups of circuit that connect with at least one of new box and merge them together
        if any([x for x in new_group if x in group]):
            merged_group = list(set(merged_group + group + new_group))
        # If the current group does not connect with one of new box then remain the same
        else:
            remaining_groups.append(group)
    # If new group of circuit doesn't exist in any current groups then append as a new group on current groups
    if len(merged_group) > 0:
        remaining_groups.append(merged_group)
    else:
        remaining_groups.append(new_group)

    change = sorted(remaining_groups) != sorted(current_groups)
    return change, remaining_groups

# Find distance of 2 boxes by coordinator 3D
def get_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def init(input_data):
    rows = input_data.split('\n')
    boxes = [list(map(int, r.split(','))) for r in rows]

    distances = []

    for i in range(0, len(boxes)-1):
        for j in range(i+1, len(boxes)):
            distances.append([i, j, get_distance(boxes[i], boxes[j])])

    distances.sort(key = lambda x: x[2])

    return boxes, distances

def part1(input_data):
    boxes, distances = init(input_data)
    i = 0
    groups = []

    # connect circuit until hit the limit
    connected_limit = 1000
    connected = 0
    while connected < connected_limit:
        connect, groups = join_circuit([distances[i][0], distances[i][1]], groups)
        connected += 1
        i += 1

    for group in groups:
        print(group)

    groups_len = list(map(len, groups))
    groups_len.sort(reverse=True)

    return groups_len[0] * groups_len[1] * groups_len[2]


def part2(input_data):
    boxes, distances = init(input_data)
    i = 0
    groups = []

    # connect circuit until all boxes are in the same group
    while not (len(groups) == 1 and len(groups[0]) == len(boxes)):
        _, groups = join_circuit([distances[i][0], distances[i][1]], groups)
        i += 1

    # return the last pair of boxes joined
    print("Last connect boxes: ",boxes[distances[i - 1][0]], boxes[distances[i - 1][1]])
    return boxes[distances[i - 1][0]][0] * boxes[distances[i - 1][1]][0]


file_object = open("input_8.txt", "r")
input_data = file_object.read()

print("Answer part1:", part1(input_data))
# 98696
print("Answer part2:", part2(input_data))
# 2245203960
