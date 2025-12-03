# https://adventofcode.com/2025/day/1#part2
import math

def rotate(current, rotation):
    rotation_step = int(rotation[1:])
    rotation_multiplier = -1 if rotation[0] == "L" else 1

    changes = rotation_multiplier * rotation_step
    new_current = current + changes

    pass_zero = math.floor(abs(new_current) / 100)

    if new_current <= 0:
        pass_zero = pass_zero + 1

    if current == 0 and new_current <0:
        pass_zero = pass_zero - 1

    return new_current % 100, pass_zero

def getPassword(input_data):
    count_zero = 0
    current = 50
    rotations = input_data.split("\n")
    for rotation in rotations:
        current, pass_zero = rotate(current, rotation)
        count_zero += pass_zero

    return count_zero


file_object = open("input_1.txt", "r")
input_data = file_object.read()

print(getPassword(input_data))
# 5820
