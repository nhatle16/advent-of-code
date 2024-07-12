# DAY 6 - ADVENT OF CODE
# https://adventofcode.com/2023/day/6

from typing import List, Tuple
import os

class Solution():
    # PART ONE
    def get_time_distance(self, file_name) -> Tuple[List[int], List[int]]:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, 'input', file_name)
        
        with open(file=input_file, mode='r') as fin:
            times = fin.readline().strip().split()[1:]
            distance = fin.readline().strip().split()[1:]
            
            times = [int(x) for x in times]
            distance = [int(x) for x in distance]
        
        return times, distance
    
    def find_ways(self, times: List[int], distance: List[int]) -> int:
        output = 1
        i, j = 0, 0     # create 2 pointers to traverse 2 lists
        
        while j < len(distance):
            time_limit = times[i]
            goal = distance[j]
            count = 0
            
            threshold = goal // time_limit + 1  # create a threshold to reduce the loop execution
            
            for k in range(threshold, time_limit - threshold + 1):
                charge, run = k, time_limit - k
                if charge * run > goal: count += 1
            
            output *= count
            i, j = i+1, j+1

        return output
    
    def solve_part1(self, file_name):
        times, distance = self.get_time_distance(file_name=file_name)
        return self.find_ways(times=times, distance=distance)
    
    
    # PART TWO
    def get_time_distance2(self, file_name) -> Tuple[int, int]:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, 'input', file_name)
        
        with open(file=input_file, mode='r') as fin:
            times = fin.readline().strip().split()[1:]
            distance = fin.readline().strip().split()[1:]

            time = int(''.join(map(str, times)))
            dist = int(''.join(map(str, distance)))
        
        return time, dist
            

    def find_ways2(self, time_limit: int, goal: int) -> int:
        threshold = goal // time_limit + 1  # create a threshold to reduce the loop execution
        count = 0
        
        # count the winning ways
        for i in range(threshold, time_limit - threshold + 1):
            if i * (time_limit - i) > goal:
                count += 1
    
        return count
    
    def solve_part2(self, file_name):
        time, dist = self.get_time_distance2(file_name=file_name)
        return self.find_ways2(time_limit=time, goal=dist)    