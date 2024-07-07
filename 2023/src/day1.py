# DAY1 - ADVENT OF CODE 2023
# https://adventofcode.com/2023/day/1

import os
class Solution():
    # PART ONE
    def calibrationValues(self, file_name) -> int:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        file_game = os.path.join(parent_dir, 'input', file_name)
        
        calibration = list()
        
        with open(file_game, 'r') as file:
            for line in file:
                first, last = None, None
                found_first = False
                
                for char in line:
                    if char.isdigit():
                        if not found_first:
                            found_first = True
                            first = char
                        last = char
                if first is not None and last is not None:
                    calibration.append(int(first+last))
                
        return sum(calibration)
    
    # PART TWO
    def calibrationValues2(self, file_name) -> int:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        file_game = os.path.join(parent_dir, 'input', file_name)
        
        calibration = list()
        
        number_dict = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0 
            }
        
        with open(file_game, 'r') as f:
            for line in f:
                first, last = None, None
                found_first = False
                word = ""

                for char in line:
                    if char.isdigit():
                        if not found_first:
                            first = int(char)
                            found_first = True
                        last = int(char)
                    elif char.isalpha():
                        word += char
                        if word in number_dict:
                            if not found_first:
                                first = number_dict[word]
                                found_first = True
                            last = number_dict[word]
                            word = ""
                    else:
                        word = ""
                        
                if first is not None and last is not None:
                    calibration.append(first * 10 + last)

        return sum(calibration)