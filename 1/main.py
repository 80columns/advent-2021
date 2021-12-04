#!/usr/bin/python

"""
 ____            _      ___
|  _ \ __ _ _ __| |_   / _ \ _ __   ___
| |_) / _` | '__| __| | | | | '_ \ / _ \
|  __/ (_| | |  | |_  | |_| | | | |  __/
|_|   \__,_|_|   \__|  \___/|_| |_|\___|

"""

input = open("input.txt")
increase_count = 0

previous_value = int(input.readline().rstrip())
line = input.readline()

while len(line) > 0:
    current_value = int(line.rstrip())

    if current_value > previous_value:
        increase_count += 1

    previous_value = current_value
    line = input.readline()

input.close()

print(increase_count)

"""
 ____            _     _____               
|  _ \ __ _ _ __| |_  |_   _|_      _____  
| |_) / _` | '__| __|   | | \ \ /\ / / _ \ 
|  __/ (_| | |  | |_    | |  \ V  V / (_) |
|_|   \__,_|_|   \__|   |_|   \_/\_/ \___/ 

"""

sliding_input = open("input.txt")
sum_increase_count = 0

value_one = int(sliding_input.readline().rstrip())
value_two = int(sliding_input.readline().rstrip())
value_three = int(sliding_input.readline().rstrip())

next_line = sliding_input.readline()

while len(next_line) > 0:
    next_value = int(next_line.rstrip())

    prior_sliding_window = value_one + value_two + value_three
    current_sliding_window = value_two + value_three + next_value

    if current_sliding_window > prior_sliding_window:
        sum_increase_count += 1

    value_one = value_two
    value_two = value_three
    value_three = next_value
    next_line = sliding_input.readline()

sliding_input.close()

print(sum_increase_count)