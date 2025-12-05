# https://adventofcode.com/2025/day/5#part2

def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = []
    for r in ranges:
        # If the merged list is empty or the current range does not overlap, then add new range to merged list.
        # As the list already sorted, so we only need to check the maximum range.
        if not merged or r[0] > merged[-1][1]:
            merged.append(r)
        # Else, merge the range by updating the end of the maximum range.
        # New range could be subset of maximum range, or could extend from maximum range
        else:
            merged[-1][1] = max(merged[-1][1], r[1])
    return merged

def count_fresh_ingredient(input_data):
    rows = input_data.split('\n')
    fresh_ingredients = []

    for row in rows:
        # Stop when finish all fresh ingredients rows
        if row == "":
            break

        fresh_ingredients.append([int(i) for i in row.split('-')])

    merged = merge_ranges(fresh_ingredients)
    count = 0

    for x in merged:
        count += (x[1] - x[0] + 1)

    return count


file_object = open("input_5.txt", "r")
input_data = file_object.read()

print("Answer:", count_fresh_ingredient(input_data))
# 352509891817881
