# DAY 8 - ADVENT OF CODE
# https://adventofcode.com/2023/day/8

from typing import List, Tuple
import os

class Solution():
    def read_file(self, file_name) -> Tuple[str, dict]:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, 'input', file_name)
        
        with open(file=input_file, mode='r') as fin:
            instruction = fin.readline().strip()
            network = dict()
            while True:
                current_line = fin.readline()
                
                if not current_line:
                    break
                
                current_line = current_line.strip()
                
                if not current_line:
                    continue 
                
                words = current_line.translate(str.maketrans('', '', '()=,')).split()
                
                k, v = words[0], (words[1], words[2])
                network[k] = v
                    
        return instruction, network
    
    def find_steps(self, inst: str, net: dict) -> int:
        step, i, n = 0, 0, len(inst)
        start = "AAA"
        while True:
            if start == "ZZZ":
                break
            command = inst[i]
            start = net[start][0] if command == 'L' else net[start][1]
            
            step += 1
            i = (i+1) % n
        return step
    
    def solve_part1(self, file_name):
        instruction, network = self.read_file(file_name=file_name)
        return self.find_steps(inst=instruction, net=network)
    
    
    
    def find_steps2(self, inst: str, net: dict) -> int:
        starts = [key for key in net.keys() if key.endswith('A')]
        step, i, n = 0, 0, len(inst)

        while True:
            if all(x.endswith('Z') for x in starts):
                break
            command = inst[i]
            if command == 'L':
                starts = [net[start][0] for start in starts]
            else:
                starts = [net[start][0] for start in starts]
                
            step += 1
            i = (i+1) % n
            
        return step
        
    def solve_part2(self, file_name):
        instruction, network = self.read_file(file_name=file_name)
        return self.find_steps2(inst=instruction, net=network)
    
if __name__ == "__main__":
    ob = Solution()
    file_name = input("Enter file name: ")
    print(ob.solve_part2(file_name))
    