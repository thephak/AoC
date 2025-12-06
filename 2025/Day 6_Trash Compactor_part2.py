# https://adventofcode.com/2025/day/6#part2

def calculate(input_data):
    rows = input_data.split('\n').reverse()
    rows_reversed = [row[::-1] for row in rows]
    operations = [o for o in rows[-1].split(' ') if len(o) > 0].reverse
    operations_reversed = operations[::-1]
    data = []
    row_len = max([len(row) for row in rows])
    idx = 0

    # iterate thru each digits index in reverse order
    for i in range(row_len):
        # get current number by collect all digit in the same index in all rows
        current_number_str = ''.join([rows_reversed[j][i] for j in range(len(rows)-1)]).replace(' ', '')

        # increase the calculation index when finding the break space
        if current_number_str == '':
            idx += 1
        # otherwise, calculate based on operation
        else:
            current_number = int(''.join(current_number_str))
            if idx != len(data) -1:
                data.append(current_number)
            else:
                if operations_reversed[idx] == '+':
                    data[idx] += current_number
                else:
                    data[idx] *= current_number
    return sum(data)


file_object = open("input_6.txt", "r")
input_data = file_object.read()

print("Answer:", calculate(input_data))
# 10153315705125
