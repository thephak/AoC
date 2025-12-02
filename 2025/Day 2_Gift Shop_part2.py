# https://adventofcode.com/2025/day/2#part2

def is_invalid_num(num):
    num_str = str(num)
    digits = len(num_str)
    mid = int(digits / 2)

    # check by splitting string number into multiple chunk by length
    for chunk_len in range(1, mid+1):
        chunks = [num_str[k:k + chunk_len] for k in range(0, len(num_str), chunk_len)]

        # number is invalid when all chunks have same value
        if len(set(chunks)) == 1:
            # print(num_str)
            return True

    return False

def invalid_sum(input_ids):
    ranges = input_ids.split(',')
    sum = 0

    for r in ranges:
        start = r.split('-')[0]
        end = r.split('-')[1]
        for i in range(int(start), int(end) + 1):
            sum += i if is_invalid_num(i) else 0
    return sum


# print(invalid_sum("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"))
# expect 4174379265
# actual 2946824823

print(invalid_sum("197-407,262128-339499,557930-573266,25-57,92856246-93001520,2-12,1919108745-1919268183,48414903-48538379,38342224-38444598,483824-534754,1056-1771,4603696-4688732,75712519-75792205,20124-44038,714164-782292,4429019-4570680,9648251-9913729,6812551522-6812585188,58-134,881574-897488,648613-673853,5261723647-5261785283,60035-128980,9944818-10047126,857821365-857927915,206885-246173,1922-9652,424942-446151,408-1000"))
