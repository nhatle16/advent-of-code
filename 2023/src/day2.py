# DAY2 - ADVENT OF CODE 2023
# https://adventofcode.com/2023/day/2

import os
class Solution():
    # PART ONE
    def sum_of_id(self, file_name) -> int:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        file_game = os.path.join(parent_dir, 'input', file_name)
        
        sum_id = 0
        with open(file_game, 'r') as f:
            for line in f:
                # Replace comma & semicolons with empty char 
                # for easier parsing and split the line
                parts = line.replace(';','').replace(',','').split()
                id = int(parts[1].rstrip(':'))  # get the game's id
                valid = True
                for i in range(2, len(parts), 2):
                    if parts[i + 1] == 'red' and int(parts[i]) > 12:
                        valid = False
                        break
                    elif parts[i + 1] == 'green' and int(parts[i]) > 13:
                        valid = False
                        break
                    elif parts[i + 1] == 'blue' and int(parts[i]) > 14:
                        valid = False
                        break
                if valid:
                    sum_id += id  
        return sum_id  
    
    # PART TWO
    def sum_of_id2(self, file_name) -> int:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        file_game = os.path.join(parent_dir, 'input', file_name)
        
        power = 0
        with open(file_game, 'r') as f:
            for line in f:
                # Replace comma & semicolons with empty char 
                # for easier parsing and split the line
                parts = line.replace(';','').replace(',','').split()
                color_dict = {'red': 0,
                              'green': 0,
                              'blue': 0}
                for i in range(2, len(parts), 2):
                    quantity = int(parts[i])
                    color = parts[i + 1]
                    color_dict[color] = max(quantity, color_dict.get(color))
                
                power += (color_dict['red'] * color_dict['green'] * color_dict['blue'])
        return power