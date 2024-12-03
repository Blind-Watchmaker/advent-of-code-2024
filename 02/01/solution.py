class Solution:

    def _parse_input(self, file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                row = [int(num) for num in line.split()]
                data.append(row)
        return data

    def _is_sorted(self, report):
        if report == sorted(report):
            return True
        if report == sorted(report, reverse=True):
            return True
        return False

    def _is_safe(self, report):
        differences = [abs(report[i+1] - report[i]) for i in range(len(report) - 1)]
        for diff in differences:
            if diff < 1 or diff > 3:
                return False
        return True
        
    def solve(self, file_path):
        data = self._parse_input(file_path)
        num_safe = 0
        for report in data:
            if self._is_sorted(report) and self._is_safe(report):
                num_safe += 1
        return num_safe

        

file_path = "input.txt"
print(Solution().solve(file_path))