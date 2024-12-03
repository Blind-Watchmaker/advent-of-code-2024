import re

class Solution:

    def _parse_input(self, file_path):
        with open(file_path, "r") as file:
            file_content = "".join(line.strip() for line in file)
        return file_content

    def _get_uncorrupted_muls(self, file_content):
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, file_content)
        return matches

    def _sum_multiplied_matches(self, matches):
        pattern = r"mul\((\d+),(\d+)\)"
        
        total = 0
        for match in matches:
            left_num, right_num = map(int, re.search(pattern, match).groups())
            result = left_num*right_num
            total += result
        return total

    def solve(self, data):
        file_content = self._parse_input(file_path)
        matches = self._get_uncorrupted_muls(file_content)
        total = self._sum_multiplied_matches(matches)
        return total
        

file_path = "input.txt"
print(Solution().solve(file_path))


