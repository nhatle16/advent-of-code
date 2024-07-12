# DAY 9 - ADVENT OF CODE
# https://adventofcode.com/2023/day/9

from typing import List

import os

class Solution():
    def read_file(self, file_name) -> List[List[int]]:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, 'input', file_name)
        
        with open(file=input_file, mode='r') as fin:
            # store changing history of each value in a list
            histories = [[int(x) for x in line.strip().split()] for line in fin.readlines()]

        return histories
    
    # PART ONE
    def extrapolate_value(self, history: List[int]) -> int:
        if all(x == history[0] for x in history):
            return history[-1]
        diffs = [history[i+1] - history[i] for i in range(len(history)-1)]
        plh = self.extrapolate_value(diffs)   # retrieve the placeholder of current sequence
        history.append(history[-1] + plh)
        return history[-1]
    
    # PART TWO
    def extrapolate_value2(self, history: List[int]) -> int:
        if all(x == history[0] for x in history):
            return history[0]
        diffs = [history[i+1] - history[i] for i in range(len(history)-1)]
        plh = self.extrapolate_value2(diffs)   # retrieve the placeholder of current sequence
        history.insert(0, history[0]-plh)
        return history[0]
    
    # Change the extrapolate function with the corresponding problem
    def sum_extrp_val(self, recs: List[List[int]]) -> int:
        output = 0
        for r in recs:
            output += self.extrapolate_value2(r)
        return output
    
    def solve_quiz(self, file_name):
        records = self.read_file(file_name=file_name)
        return self.sum_extrp_val(recs=records)