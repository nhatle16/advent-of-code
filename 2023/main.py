from src.day1 import Solution
from src.day2 import Solution
from src.day3 import Part1, Part2
from src.day4 import Solution
from src.day5 import Solution 

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    ob = Solution()
    print(ob.solve_part1(file_name=file_name))