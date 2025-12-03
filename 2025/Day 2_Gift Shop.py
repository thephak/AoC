# https://adventofcode.com/2025/day/2

def is_invalid_num(num):
    num_str = str(num)
    mid = int(len(num_str) / 2)

    # number is invalid when first half and second half are the same
    return num_str[:mid] == num_str[mid:]

def invalid_sum(input_ids):
    ranges = input_ids.split(',')
    sum = 0

    for r in ranges:
        start = r.split('-')[0]
        end = r.split('-')[1]
        for i in range(int(start), int(end) + 1):
            sum += i if is_invalid_num(i) else 0
    return sum


file_object = open("input_2.txt", "r")
input_data = file_object.read()
print(invalid_sum(input_data))

# 19128774598