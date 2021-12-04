#!/usr/bin/python

'''
 mmmmm                  m           mmm
 #   "#  mmm    m mm  mm#mm           #
 #mmm#" "   #   #"  "   #             #
 #      m"""#   #       #             #
 #      "mm"#   #       "mm         mm#mm

'''

input = open("input.txt")
horizontal_position = 0
depth = 0

line = input.readline().rstrip()

while len(line) > 0:
    if line.startswith("f"):
        horizontal_position += int(line[-1])
    elif line.startswith("u"):
        depth -= int(line[-1])
    elif line.startswith("d"):
        depth += int(line[-1])

    line = input.readline().rstrip()

input.close()

print(horizontal_position * depth)

'''
 mmmmm                  m            mmmm
 #   "#  mmm    m mm  mm#mm         "   "#
 #mmm#" "   #   #"  "   #               m"
 #      m"""#   #       #             m"
 #      "mm"#   #       "mm         m#mmmm

'''

input = open("input.txt")
horizontal_position = 0
depth = 0
aim = 0

line = input.readline().rstrip()

while len(line) > 0:
    if line.startswith("f"):
        horizontal_position += int(line[-1])
        depth += aim * int(line[-1])
    elif line.startswith("u"):
        aim -= int(line[-1])
    elif line.startswith("d"):
        aim += int(line[-1])

    line = input.readline().rstrip()

input.close()

print(horizontal_position * depth)