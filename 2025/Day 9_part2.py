# https://adventofcode.com/2025/day/9
from shapely.geometry import Polygon, box
import math
import itertools as it

def x(input_data):

    rows = input_data.split("\n")
    red = set(tuple(map(int, x.split(','))) for x in rows)

    poly = Polygon(red)
    res = 0
    res2 = 0
    for x, y in red:
        for xx, yy in red:
            res = max((abs(x - xx) + 1) * (abs(y - yy) + 1), res)
            if poly.contains(box(x, y, xx, yy)):
                res2 = max((abs(x - xx) + 1) * (abs(y - yy) + 1), res2)
    print(res)
    print(res2)


def get_size(a,b):
    return (abs(a[0] - b[0])+1) * (abs(a[1] - b[1]) + 1)

def is_valid_area(coords_red_list, corners_list, a, b):
    return (
            # a in corners_list
            # and b in corners_list
            # and
        ((a[0], b[1]) in corners_list
            or (b[0], a[1]) in corners_list)
            # check diagonal
            and
            ((a in coords_red_list and b in coords_red_list)
                 or ((a[0], b[1]) in coords_red_list and (b[0], a[1]) in coords_red_list)
    ))

def part1(input_data):
    rows = input_data.split('\n')
    coords_red = set(tuple(map(int,x.split(','))) for x in rows)


    coords_red_list = list(coords_red)
    # print(coords_red_list)
    new_coords = []
    for i in range(0, len(coords_red_list) - 1):
        for j in range(i + 1, len(coords_red_list)):
            if coords_red_list[i][0] == coords_red_list[j][0] and coords_red_list[i][1] != coords_red_list[j][1]:
                mn = min(coords_red_list[i][1], coords_red_list[j][1])
                mx = max(coords_red_list[i][1], coords_red_list[j][1])

                for k in range(mn+1,mx):
                    new_coords.append((coords_red_list[i][0], k))
            elif coords_red_list[i][1] == coords_red_list[j][1] and coords_red_list[i][0] != coords_red_list[j][0]:
                mn = min(coords_red_list[i][0], coords_red_list[j][0])
                mx = max(coords_red_list[i][0], coords_red_list[j][0])

                for k in range(mn + 1, mx):
                    new_coords.append((k, coords_red_list[i][1]))
    corners = set(coords_red).union(new_coords)
    corners_list = list(corners)
    print("len corners:",len(corners_list))

    max_x = max([n[0] for n in coords_red])
    max_y = max([n[1] for n in coords_red])
    for j in range(max_y+1):
        lines = ""
        for i in range(max_x+1):
            if (i,j) in coords_red_list:
                lines += "#"
            elif (i,j) in corners_list:
                lines += "X"
            else:
                lines += "."
        print(lines)

    distances = []
    for i in range(0, len(corners_list)-1):
        for j in range(i+1, len(corners_list)):
            # print("check corners_list[i]:", corners_list[i], " corners_list[j]:", corners_list[j])
            if is_valid_area(coords_red_list, corners_list, corners_list[i], corners_list[j]):
                new_area = get_size(corners_list[i], corners_list[j])
                print("corners_list[i]:",corners_list[i]," corners_list[j]:", corners_list[j]," new_area:",new_area)
                distances.append([corners_list[i], corners_list[j], new_area])

    distances.sort(key=lambda x: x[2], reverse=True)
    print(distances)

    return distances[0][2]

file_object = open("input_9.txt", "r")
input_data = file_object.read()

print("Answer part1:", x(input_data))
# 740051 low
# 657984 

# print("Answer part2:", part2(input_data))

