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


print(invalid_sum("197-407,262128-339499,557930-573266,25-57,92856246-93001520,2-12,1919108745-1919268183,48414903-48538379,38342224-38444598,483824-534754,1056-1771,4603696-4688732,75712519-75792205,20124-44038,714164-782292,4429019-4570680,9648251-9913729,6812551522-6812585188,58-134,881574-897488,648613-673853,5261723647-5261785283,60035-128980,9944818-10047126,857821365-857927915,206885-246173,1922-9652,424942-446151,408-1000"))
# 19128774598