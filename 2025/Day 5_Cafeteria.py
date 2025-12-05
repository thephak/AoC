# https://adventofcode.com/2025/day/5

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
    merged = []

    count = 0
    for row in rows:
        # When all fresh ingredients rows read, merge the fresh ingredients ranges
        if row == "":
            merged = merge_ranges(fresh_ingredients)
        # Fresh ingredients rows: add to fresh ingredients ranges
        elif row.find('-') != -1:
            fresh_ingredients.append([int(i) for i in row.split('-')])
        # Available ingredient rows: check if the ingredient presented in any merged fresh ingredients range
        else:
            if any(m for m in merged if m[0] <= int(row) <= m[1]):
                count += 1

    return count


file_object = open("input_5.txt", "r")
input_data = file_object.read()

print("Answer:", count_fresh_ingredient(input_data))
# 674
