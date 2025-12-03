# https://adventofcode.com/2025/day/3

def recur(current, remaining, digits_remain):
    if digits_remain == 0:
        return int(current)
    if len(remaining) == digits_remain:
        return int(current + remaining)

    max_value = max([int(x) for idx, x in enumerate(remaining) if idx <= len(remaining) - digits_remain])
    max_idx = remaining.index(str(max_value))
    return recur(current + str(max_value), remaining[max_idx+1:], digits_remain - 1)

def joltage(input_data, digits):
    rows = input_data.split('\n')
    return sum([recur("", row, digits) for row in rows])


file_object = open("input_3.txt", "r")
input_data = file_object.read()

# for part 1
print("Answer:", joltage(input_data, 2))
# 17193

# for part 2
print("Answer:", joltage(input_data, 12))
# 171297349921310