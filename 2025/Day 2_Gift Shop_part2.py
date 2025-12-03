# https://adventofcode.com/2025/day/2#part2

def is_invalid_num(num):
    num_str = str(num)
    mid = int(len(num_str) / 2)

    # check by splitting string number into multiple chunk by length
    for chunk_len in range(1, mid+1):
        chunks = [num_str[k:k + chunk_len] for k in range(0, len(num_str), chunk_len)]

        # number is invalid when all chunks have same value
        if len(set(chunks)) == 1:
            # print(num_str)
            return True

    return False

def invalid_sum(input_data):
    ranges = input_data.split(',')
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
# 21932258645