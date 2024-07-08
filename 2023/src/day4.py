# DAY 4 - ADVENT OF CODE
# https://adventofcode.com/2023/day/4

import os

class Solution():
    def __init__(self, file_name):
        self.__cards = None
        
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, 'input', file_name)
        
        with open (file=input_file, mode='r') as fin:
            # Get the information of the scratchcards
            # regardless of card numbers
            self.__cards = [list(line.strip()[line.find(':')+1:].split()) for line in fin]
    
    # PART ONE
    def calculate_points(self):
        points = 0
        
        for card in self.__cards:
            bar = card.index('|')
            
            win_numbers = card[:bar]
            own_numbers = card[bar+1:]
            
            i = 0     # Create 2 pointers to traverse 2 lists
            count = 0
            first = False   # Create a flag
            
            while i < len(win_numbers):
                if win_numbers[i] in own_numbers:
                    if not first:
                        count = 1
                        first = True    # Set flag into True
                    else: 
                        count *= 2  # Each match after that makes the point doubled
                i += 1
            points += count
            
        return points
    
    # PART TWO
    def count_scratchcards(self):
        card_dict = dict()
        ord = 1
        
        for card in self.__cards:
            bar = card.index('|')
            
            win_numbers = card[:bar]
            own_numbers = card[bar+1:]
            
            count = 0   
            
            for i in range(len(win_numbers)):
                if win_numbers[i] in own_numbers:
                    count += 1
                    
            card_dict[ord] = [count, 1]     # First element is matches, second element is number of copy
            ord += 1
        
        # Go through each key in the dictionary
        for k in range(1, len(card_dict)+1):
            matches, copies = card_dict[k]  
            # Access the subordinates of current card
            # subordinates are cards to be added copies that lie
            # within the number of matches of current card
            for i in range(1, matches+1):
                if k + i in card_dict:
                    card_dict[k+i][1] += copies     # Add current card number of copies to the copies of its subordinates
                                                    
        
        total = sum(copies for (matches, copies) in card_dict.values())
        return total
    
    def solve_part1(self):
        return self.calculate_points()
    
    def solve_part2(self):
        return self.count_scratchcards()
 