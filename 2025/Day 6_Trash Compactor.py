# https://adventofcode.com/2025/day/6
import operator

ops = { "+": operator.add, "*": operator.mul }

def calculate(input_data):
    rows = input_data.split('\n')
    operations = [ops[o] for o in rows[-1].split(' ') if len(o) > 0]
    data = []

    # iterate thru each row
    for i, row in enumerate(rows):
        # skip last operation row
        if i >= len(rows) -1:
            break

        current_nums = [int(n) for n in row.split(' ') if len(n) > 0]
        if i == 0:
            data.extend(current_nums)
        # if not the first number to process, then calculate based on operation
        else:
            # iterate thru each number in the row
            for j, num in enumerate(current_nums):
                data[j] = operations[j](data[j], num)

    return sum(data)


file_object = open("input_6.txt", "r")
input_data = file_object.read()

print("Answer:", calculate(input_data))
# 5595593539811
