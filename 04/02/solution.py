import re

class Solution:

    def __init__(self, word):
        self.word = word
        self._reversed_word = word[::-1]

    def _parse_input(self, file_path):
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines

    def _find_crossing_diagonals(self, lines):
        rows = len(lines)
        cols = len(lines[0])
        intersections = []

        # Iterate over possible centers of crossing diagonals
        for i in range(1, rows - 1):  # Avoid edges as the center needs neighbors
            for j in range(1, cols - 1):  # Avoid edges as the center needs neighbors
                # Top-left to bottom-right
                diag1 = lines[i - 1][j - 1] + lines[i][j] + lines[i + 1][j + 1]
                # Top-right to bottom-left
                diag2 = lines[i - 1][j + 1] + lines[i][j] + lines[i + 1][j - 1]
                
                # Add both diagonals if they intersect
                intersections.append((diag1, diag2))

        return intersections

    def _count_x_mas_occurrences(self, intersections):
        total = 0
        for d1, d2 in intersections:
            if d1 == self.word or d1 == self._reversed_word:
                if d2 == self.word or d2 == self._reversed_word:
                        total += 1
        return total
                    

    def solve(self, file_path):
        lines = self._parse_input(file_path)
        intersections = self._find_crossing_diagonals(lines)        
        return self._count_x_mas_occurrences(intersections)

file_path = "input.txt"
print(Solution(word="MAS").solve(file_path))