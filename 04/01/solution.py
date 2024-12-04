import re

class Solution:

    def __init__(self, word):
        self.word = word
        self._reversed_word = word[::-1]
        self._pattern = rf"{self.word}"
        self._reversed_pattern = rf"{self._reversed_word}"

    def _parse_input(self, file_path):
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines

    def _count_occurrences(self, lines):
        total = 0
        for line in lines:
            num_matches = len(re.findall(self._pattern, line))
            total += num_matches
            num_matches = len(re.findall(self._reversed_pattern, line))
            total += num_matches
        return total

    def _count_horizontal_occurrences(self, lines):
        return self._count_occurrences(lines)

    def _count_vertical_occurrences(self, lines):
        columns = ["".join(column) for column in zip(*lines)]
        return self._count_occurrences(columns)

    def _get_all_diagonals(self, lines):
        rows = len(lines)
        cols = len(lines[0])

        diagonals_tl_br = []  # Top-left to bottom-right (\)
        diagonals_tr_bl = []  # Top-right to bottom-left (/)

        # Top-left to bottom-right (\ direction)
        for d in range(rows + cols - 1):
            diagonal = []
            for row in range(rows):
                col = d - row
                if 0 <= col < cols:
                    diagonal.append(lines[row][col])
            if diagonal:
                diagonals_tl_br.append("".join(diagonal))

        # Top-right to bottom-left (/ direction)
        for d in range(-cols + 1, rows):
            diagonal = []
            for row in range(rows):
                col = row - d
                if 0 <= col < cols:
                    diagonal.append(lines[row][col])
            if diagonal:
                diagonals_tr_bl.append("".join(diagonal))

        return diagonals_tl_br, diagonals_tr_bl

    def _count_diagonal_occurrences(self, lines):
        diagonals_tl_br, diagonals_tr_bl = self._get_all_diagonals(lines)
        total = 0
        total += self._count_occurrences(diagonals_tl_br)
        total += self._count_occurrences(diagonals_tr_bl)
        return total

    def solve(self, file_path):
        lines = self._parse_input(file_path)
        total = 0
        total += self._count_horizontal_occurrences(lines)
        total += self._count_vertical_occurrences(lines)
        total += self._count_diagonal_occurrences(lines)
        return total

file_path = "input.txt"
print(Solution(word="XMAS").solve(file_path))