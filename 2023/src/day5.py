# DAY 5 - ADVENT OF CODE
# https://adventofcode.com/2023/day/5

from typing import List, Tuple
import os

class Solution():
    def calculate_dest(self, src: int, start_des: int, start_src: int, range: int) -> Tuple[int, bool]:
        '''
        Find the corresponding destination spot of the source, has a flag to show succesful conversion
        '''        
        if start_src + range <= src or src < start_src:
            return src, False
        return src - (start_src - start_des), True
    
    def get_seed(self, line: str) -> List[int]:
        '''
        Retrieve the list of seed numbers to be planted
        '''        
        return [int(x) for x in line.split()[1:]]
    
    def solve_part1(self, file_name) -> List[int]:
        # Retrieve the path to input file from another package
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, 'input', file_name)
        
        with open(file=input_file, mode='r') as fin:
            # First line contains the seed numbers
            seeds = self.get_seed(fin.readline().strip())
            while True:
                current_line = fin.readline()

                # Check if it reads the end of file
                if not current_line:
                    break
                
                # Remove the endline character
                current_line = current_line.strip()
        
                if current_line.endswith("map:"):
                    maps = []
                    
                    # Dive into the maps and retrieve information
                    while True:
                        current_line = fin.readline().strip()
                        if not current_line:
                            break
                        numbers = [int(x) for x in current_line.split()]
                        maps.append(numbers)
                    
                    for i in range(len(seeds)):
                        for line in maps:
                            dest, flag = self.calculate_dest(src=seeds[i], start_des=line[0], start_src=line[1], range=line[2])
                            if flag:
                                seeds[i] = dest
                                break            
                        
        return min(seeds) 