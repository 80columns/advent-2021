#!/usr/bin/python

"""
 _          _        
|_)_..__|_ / \._  _  
| (_||  |_ \_/| |(/_

"""

input = open("input.txt")

fuel = 0
val_list = [int(x) for x in input.readline().split(",")]
val_list.sort()

position = val_list[(len(val_list) // 2) - 1]

for x in val_list:
    fuel += abs(x - position)

print(fuel)

"""
 _         ___       
|_)_..__|_  |     _  
| (_||  |_  |\/\/(_)

"""

def calculate_fuel(val_list, position):
    fuel = 0

    for x in val_list:
        n = abs(x - position)
        fuel += (n * (n + 1)) // 2

    return fuel

lower_position = sum(val_list) // len(val_list)
lower_fuel = calculate_fuel(val_list, lower_position)
upper_fuel = calculate_fuel(val_list, lower_position + 1)

print(lower_fuel if lower_fuel < upper_fuel else upper_fuel)