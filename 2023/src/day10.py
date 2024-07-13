# DAY 10 - ADVENT OF CODE
# https://adventofcode.com/2023/day/10

from typing import List, Tuple
from collections import deque
import os

connections = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
    '.': []
}

class Solution():
    def __init__(self, file):
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        input_file = os.path.join(parent_dir, 'input', file)
        
        with open (file=input_file, mode='r') as fin:
            self.sketch = fin.read().strip().split('\n')
            
            for i, line in enumerate(self.sketch):
                if 'S' in line:
                    self.spos = (i, line.index('S'))
    
    def get_dir_s(self, i: int, j: int) -> List[Tuple[int, int]]:
        '''
        Retrieve the directions to the neighbor of S
        '''
        res = []
        n, m = len(self.sketch), len(self.sketch[0])
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ii, jj = i + di, j + dj
            if not (0 <= ii < n and 0 <= jj < m):
                continue
            if (i, j) in self.get_nbrs(ii, jj):     # check if S is a neighbor of its neighbor
                res.append((di, dj))
        return res
    
    def get_nbrs(self, i: int, j: int) -> List[Tuple[int, int]]:
        '''
        Retrieve the position of neighbors of the current position
        '''   
        res, directions = [], []
        n, m = len(self.sketch), len(self.sketch[0])
        if self.sketch[i][j] == 'S':
            directions = self.get_dir_s(i, j)
        else:
            directions = connections[self.sketch[i][j]]
        for di, dj in directions:
            ii, jj = i + di, j + dj
            if not (0 <= ii < n and 0 <= jj < m):
                continue
            res.append((ii, jj))
        return res

    def find_farthest_path(self) -> int:
        dists = dict()
        visited = set()
        q = deque([(self.spos, 0)])
        
        while len(q) > 0:
            point, dist = q.popleft()
            if point in visited:
                continue
            visited.add(point)
            dists[point] = dist
            
            for nbr in self.get_nbrs(*point):
                if nbr not in visited:  # avoid turning back to old position
                    q.append((nbr, dist + 1))
                    
        return max(dists.values())
    
    def solve_part1(self):
        return self.find_farthest_path()