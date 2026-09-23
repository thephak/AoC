# https://adventofcode.com/2025/day/9

import math

def get_size(a,b):
    return (abs(a[0] - b[0])+1) * (abs(a[1] - b[1]) + 1)

def part1(input_data):
    rows = input_data.split('\n')
    coords = [list(map(int,x.split(','))) for x in rows]
    print(coords)

    distances = []

    for i in range(0, len(coords)-1):
        for j in range(i+1, len(coords)):
            distances.append([coords[i], coords[j], get_size(coords[i], coords[j])])

    distances.sort(key=lambda x: x[2], reverse=True)
    print(distances)

    return distances[0][2]

file_object = open("input_9.txt", "r")
input_data = file_object.read()

print("Answer part1:", part1(input_data))
# 4767418746

# print("Answer part2:", part2(input_data))

