#!/usr/bin/python

def grow_fish(fish, days):
    fish_dict = {}
    total_fish = 0

    for x in range(9):
        fish_dict[x] = 0

    for f in fish:
        fish_dict[f] += 1

    for x in range(days):
        new_zero_fish = fish_dict[1]
        fish_dict[1] = 0

        for f in range(2, 9):
            moving_fish = fish_dict[f]
            fish_dict[f] = 0
            fish_dict[f - 1] += moving_fish

        zero_count = fish_dict[0]
        fish_dict[6] += zero_count
        fish_dict[8] += zero_count
        fish_dict[0] = new_zero_fish

    for x in range(9):
        total_fish += fish_dict[x]

    return total_fish

def main():
    input = open("input.txt")
    fish = [int(x) for x in input.readline().split(",")]
    
    """
        _/_/_/                          _/            _/_/                       
       _/    _/    _/_/_/  _/  _/_/  _/_/_/_/      _/    _/  _/_/_/      _/_/    
      _/_/_/    _/    _/  _/_/        _/          _/    _/  _/    _/  _/_/_/_/   
     _/        _/    _/  _/          _/          _/    _/  _/    _/  _/          
    _/          _/_/_/  _/            _/_/        _/_/    _/    _/    _/_/_/

    """

    print(grow_fish(fish, 80))

    """
        _/_/_/                          _/          _/_/_/_/_/                               
       _/    _/    _/_/_/  _/  _/_/  _/_/_/_/          _/      _/      _/      _/    _/_/    
      _/_/_/    _/    _/  _/_/        _/              _/      _/      _/      _/  _/    _/   
     _/        _/    _/  _/          _/              _/        _/  _/  _/  _/    _/    _/    
    _/          _/_/_/  _/            _/_/          _/          _/      _/        _/_/

    """

    print(grow_fish(fish, 256))

if __name__ == "__main__":
    main()