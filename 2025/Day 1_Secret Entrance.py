# https://adventofcode.com/2025/day/1

def rotate(current, rotation = ""):
    rotation_step = int(rotation[1:])
    rotation_multiplier = -1 if rotation[0] == "L" else 1
    return (current + (rotation_multiplier * rotation_step)) % 100

def getPassword(input_data):
    count_zero = 0
    current = 50
    rotations = input_data.split("\n")
    for rotation in rotations:
        current = rotate(current, rotation)
        count_zero += int(current == 0)
    return count_zero


file_object = open("input_1.txt", "r")
input_data = file_object.read()

print(getPassword(input_data))
# 1007
