#!/usr/bin/python

from collections import namedtuple

"""
  _ \            |     _ \             
 |   | _` |  __| __|  |   | __ \   _ \ 
 ___/ (   | |    |    |   | |   |  __/ 
_|   \__,_|_|   \__| \___/ _|  _|\___|

"""

input = open("input.txt")
lines = input.readlines()
horizontal_vertical_lines = []
coordinate_pair = namedtuple('coordinate_pair', ['x1', 'y1', 'x2', 'y2'])
overlapping_coordinate_count = 0

for line in lines:
    line_parts = line.split(" -> ")
    first_coordinate = line_parts[0].split(",")
    second_coordinate = line_parts[1].split(",")

    x1 = int(first_coordinate[0])
    y1 = int(first_coordinate[1])
    x2 = int(second_coordinate[0])
    y2 = int(second_coordinate[1])

    if x1 == x2 or y1 == y2:
        horizontal_vertical_lines.append(coordinate_pair(x1, y1, x2, y2))

grid = {}

for item in horizontal_vertical_lines:
    if item.x1 == item.x2:
        # traverse the line on the y-axis
        lower_y = item.y1 if item.y1 < item.y2 else item.y2
        upper_y = item.y1 if item.y1 > item.y2 else item.y2

        for y_coord in range(lower_y, upper_y + 1):
            if (item.x1, y_coord) in grid:
                grid[(item.x1, y_coord)] += 1
            else:
                grid[(item.x1, y_coord)] = 1
    elif item.y1 == item.y2:
        # traverse the line on the x-axis
        lower_x = item.x1 if item.x1 < item.x2 else item.x2
        upper_x = item.x1 if item.x1 > item.x2 else item.x2

        for x_coord in range(lower_x, upper_x + 1):
            if (x_coord, item.y1) in grid:
                grid[(x_coord, item.y1)] += 1
            else:
                grid[(x_coord, item.y1)] = 1

for coordinate in grid:
    if grid[coordinate] > 1:
        overlapping_coordinate_count += 1

print(overlapping_coordinate_count)

"""
  _ \            |   __ __|              
 |   | _` |  __| __|    |\ \  \   / _ \  
 ___/ (   | |    |      | \ \  \ / (   | 
_|   \__,_|_|   \__|   _|  \_/\_/ \___/

"""

diagonal_lines = []
overlapping_coordinate_count = 0

for line in lines:
    line_parts = line.split(" -> ")
    first_coordinate = line_parts[0].split(",")
    second_coordinate = line_parts[1].split(",")

    x1 = int(first_coordinate[0])
    y1 = int(first_coordinate[1])
    x2 = int(second_coordinate[0])
    y2 = int(second_coordinate[1])

    if x1 != x2 and y1 != y2:
        diagonal_lines.append(coordinate_pair(x1, y1, x2, y2))

for item in diagonal_lines:
    # traverse the line on the x-axis and y-axis
    x_increment = 1 if item.x1 < item.x2 else -1
    y_increment = 1 if item.y1 < item.y2 else -1

    x_start = item.x1
    y_start = item.y1

    x_end = item.x2
    y_end = item.y2

    while x_start != (x_end + x_increment) and y_start != (y_end + y_increment):
        if (x_start, y_start) in grid:
            grid[(x_start, y_start)] += 1
        else:
            grid[(x_start, y_start)] = 1

        x_start += x_increment
        y_start += y_increment

for coordinate in grid:
    if grid[coordinate] > 1:
        overlapping_coordinate_count += 1

print(overlapping_coordinate_count)