# # DAY3 - ADVENT OF CODE
# # https://adventofcode.com/2023/day/3

from typing import List

# PART ONE
class Part1():    
    def __init__(self, file_name):
        with open(file=file_name, mode='r') as f:
            self.schematic = [list(line.strip()) for line in f]
            self.n = len(self.schematic)
            self.m = len(self.schematic[0])
            
    def is_symbol(self, i: int, j: int) -> bool:
        if not (0 <= i < self.n and 0 <= j < self.m):
            return False
        return self.schematic[i][j] != '.' and not self.schematic[i][j].isdigit()

    def sum_part_numbers(self) -> int:
        sum = 0
        for i, line in enumerate(self.schematic):
            start = 0   # retrieve the index of a digit
            j = 0
            while j < self.m:
                start = j
                num = ""
                while j < self.m and line[j].isdigit():
                    num += line[j]
                    j += 1
                if num == "":
                    j += 1
                    continue
                
                num = int(num)
                
                # check the left and right side on the same row
                if self.is_symbol(i, start-1) or self.is_symbol(i, j):
                    sum += num
                    j += 1
                    continue    # exit the loop and look for the next digit
                
                # check the adjacent tiles on top and botton
                for k in range(start-1, j+1):
                    if self.is_symbol(i-1, k) or self.is_symbol(i+1, k):
                        sum += num
                        break
        return sum
    

# PART TWO
class Part2():    
    def __init__(self, file_name):
        with open (file=file_name, mode='r') as fin:
            self.schematic = [list(line.strip()) for line in fin]
            self.n = len(self.schematic)
            self.m = len(self.schematic[0])
            self.tuples_value = [[list() for _ in range(self.m)] for _ in range(self.n)]
            
    def is_symbol(self, i: int, j: int, num: int) -> bool:
        if not (0 <= i < self.n and 0 <= j < self.m):
            return False
        if self.schematic[i][j] == '*':
            self.tuples_value[i][j].append(num)
        return self.schematic[i][j] != '.' and not self.schematic[i][j].isdigit()

    def sum_part_numbers(self) -> int:
        sum = 0
        for i, line in enumerate(self.schematic):
            start = 0   # retrieve the index of a digit
            j = 0
            while j < self.m:
                start = j
                num = ""
                while j < self.m and line[j].isdigit():
                    num += line[j]
                    j += 1
                if num == "":
                    j += 1
                    continue
                
                num = int(num)
                
                # check the left and right side on the same row
                # if there is an '*', store the current number
                self.is_symbol(i, start-1, num) or self.is_symbol(i, j, num)
                
                # check the adjacent tiles on top and botton
                for k in range(start-1, j+1):
                    self.is_symbol(i-1, k, num) or self.is_symbol(i+1, k, num)
        
        for i in range(self.n):
            for j in range(self.n):
                nums = self.tuples_value[i][j]
                if self.schematic[i][j] == '*' and len(nums) == 2:
                    sum += (nums[0] * nums[1])  
        
        return sum
    
if __name__ == "__main__":
    file_name = "aoc3.txt"
    ob1 = Part1(file_name=file_name)
    print(ob1.sum_part_numbers())
    ob2 = Part2(file_name=file_name)
    print(ob2.sum_part_numbers())