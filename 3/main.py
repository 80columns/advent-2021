#!/usr/bin/python

"""
 , __                    __
/|/  \                  /\_\/
 |___/ __,   ,_  _|_   |    | _  _    _
 |    /  |  /  |  |    |    |/ |/ |  |/
 |    \_/|_/   |_/|_/   \__/   |  |_/|__/

"""

input = open("input.txt")
gamma_rate = ""
epsilon_rate = ""

line = input.readline().rstrip()
bit_counts = [0 for x in range(len(line))]

while len(line) > 0:
    for x in range(len(line)):
        if line[x] == "0":
            bit_counts[x] -= 1
        else:
            bit_counts[x] += 1

    line = input.readline().rstrip()

for x in bit_counts:
    if x > 0:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

input.close()

print(gamma_rate * epsilon_rate)

"""
 , __                   ______
/|/  \                 (_) |
 |___/ __,   ,_  _|_       |         __
 |    /  |  /  |  |      _ ||  |  |_/  \_
 |    \_/|_/   |_/|_/   (_/  \/ \/  \__/

"""

input = open("input.txt")
oxygen_generator_rating = 0
co2_scrubber_rating = 0
oxygen_generator_rating_vals = None
co2_scrubber_rating_vals = None

numbers = [x.rstrip() for x in input.readlines()]
input.close()

index = 0
index_count = 0
index_one_matches = []
index_zero_matches = []

for x in numbers:
    if x[index] == "0":
        index_count -= 1
        index_zero_matches.append(x)
    else:
        index_count += 1
        index_one_matches.append(x)

if index_count >= 0:
    oxygen_generator_rating_vals = index_one_matches
    co2_scrubber_rating_vals = index_zero_matches
else:
    oxygen_generator_rating_vals = index_zero_matches
    co2_scrubber_rating_vals = index_one_matches

index = 1

while len(oxygen_generator_rating_vals) > 1:
    index_count = 0
    index_zero_matches = []
    index_one_matches = []

    for x in oxygen_generator_rating_vals:
        if x[index] == "0":
            index_count -= 1
            index_zero_matches.append(x)
        else:
            index_count += 1
            index_one_matches.append(x)

    if index_count >= 0:
        oxygen_generator_rating_vals = index_one_matches
    else:
        oxygen_generator_rating_vals = index_zero_matches

    index += 1

index = 1

while len(co2_scrubber_rating_vals) > 1:
    index_count = 0
    index_zero_matches = []
    index_one_matches = []

    for x in co2_scrubber_rating_vals:
        if x[index] == "0":
            index_count -= 1
            index_zero_matches.append(x)
        else:
            index_count += 1
            index_one_matches.append(x)

    if index_count < 0:
        co2_scrubber_rating_vals = index_one_matches
    else:
        co2_scrubber_rating_vals = index_zero_matches

    index += 1

oxygen_generator_rating = int(oxygen_generator_rating_vals[0], 2)
co2_scrubber_rating = int(co2_scrubber_rating_vals[0], 2)

print(oxygen_generator_rating * co2_scrubber_rating)