# DAY 7 - ADVENT OF CODE
# https://adventofcode.com/2023/day/7

from collections import Counter
from typing import List, Tuple
from functools import cmp_to_key

import os

class Solution():
    # PART ONE
    def get_strength(self, label: str) -> int:
        return int(label) if label.isdigit() else {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}.get(label, 0)
    
    def type_strength(self, type: str) -> int:
        return {"five": 6, "four": 5, "full": 4, "three": 3, "two": 2, "one": 1, "high": 0}.get(type)
    
    def get_hands_bids(self, file_name) -> List[Tuple[str, int]]:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, "input", file_name)
        
        with open(file=input_file, mode='r') as fin:
            return [(line.split()[0], int(line.split()[1])) for line in fin]
    
    def categorize_hand(self, hand: str) -> str:
        card_count = Counter(hand)
        l = len(card_count)
        if l == 5:
            return "high"
        elif l == 4:
            return "one"
        elif l == 3:
            return "two" if 2 in card_count.values() else "three"
        elif l == 2:
            return "full" if 3 in card_count.values() else "four"
        else:
            return "five"     
    
    def compare_hands(self, pair1: Tuple[str, int], pair2: Tuple[str, int]) -> int:
        hand1, hand2 = pair1[0], pair2[0]
        for i in range(len(hand1)):
            if self.get_strength(hand1[i]) < self.get_strength(hand2[i]):
                return 1
            elif self.get_strength(hand1[i]) > self.get_strength(hand2[i]):
                return -1
        return 0            
    
    def find_total_winnings(self, pairs: List[Tuple[str, int]]) -> dict:
        ctgs = {}
        
        for hand, bid in pairs:
            type = self.categorize_hand(hand)
            if type not in ctgs:
                ctgs[type] = list()
            ctgs[type].append((hand, bid))
        
        rank = len(pairs)  
        output = 0
        
        for type in sorted(ctgs.keys(), key=self.type_strength, reverse=True):
            hands_sorted = sorted(ctgs[type], key=cmp_to_key(self.compare_hands))  # sort hands in increasing order
            for i, (hand, bid) in enumerate(hands_sorted):
                output += bid * rank
                rank -= 1
                
        return output
    
    def solve_part1(self, file_name):
        pairs = self.get_hands_bids(file_name=file_name)
        return self.find_total_winnings(pairs)
    
    # PART TWO
    def get_strength2(self, label: str) -> int:
        return int(label) if label.isdigit() else {'A': 13, 'K': 12, 'Q': 11, 'T': 10, 'J': 1}.get(label, 0)
    
    def categorize_hand2(self, hand: str) -> str:
        if 'J' not in hand:
            return self.categorize_hand(hand)
        
        j_freq = hand.count('J')
        labels = sorted(Counter(hand).values(), reverse=True)
        
        if j_freq == 5:
            return "five"
        if j_freq == 4:
            return "five"
        elif j_freq == 3:
            if labels == [3,2]:
                return "five"
            return "four"
        elif j_freq == 2:
            if labels == [3,2]:
                return "five"
            elif labels == [2,2,1]:
                return "four"
            return "three"
        else:
            if labels == [4,1]:
                return "five"
            elif labels == [3,1,1]:
                return "four"
            elif labels == [2,2,1]:
                return "full"
            elif labels == [2,1,1,1]:
                return "three"
            return "one"

    def compare_hands2(self, pair1: Tuple[str, int], pair2: Tuple[str, int]) -> int:
        hand1, hand2 = pair1[0], pair2[0]
        for i in range(len(hand1)):
            if self.get_strength2(hand1[i]) < self.get_strength2(hand2[i]):
                return 1
            elif self.get_strength2(hand1[i]) > self.get_strength2(hand2[i]):
                return -1
        return 0
        
    def find_total_winnings2(self, pairs: List[Tuple[str, int]]) -> dict:
        ctgs = {}
        
        for hand, bid in pairs:
            type = self.categorize_hand2(hand)
            if type not in ctgs:
                ctgs[type] = list()
            ctgs[type].append((hand, bid))
            
        rank = len(pairs)  
        output = 0
        
        for type in sorted(ctgs.keys(), key=self.type_strength, reverse=True):
            hands_sorted = sorted(ctgs[type], key=cmp_to_key(self.compare_hands2))  # sort hands in increasing order
            for i, (hand, bid) in enumerate(hands_sorted):
                output += bid * rank
                rank -= 1
                
        return output

    def solve_part2(self, file_name):
        pairs = self.get_hands_bids(file_name=file_name)
        return self.find_total_winnings2(pairs)