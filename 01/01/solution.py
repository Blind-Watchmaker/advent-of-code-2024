class Solution:

    def _parse_input(self, file_path):
        left_list = []
        right_list = []
        with open(file_path, "r") as file:
            for line in file:
                left_num, right_num = line.split("   ")  
                left_list.append(int(left_num.strip()))
                right_list.append(int(right_num.strip()))
        left_list.sort()
        right_list.sort()
        return left_list, right_list

    def _sum_of_absolute_differences(self, left_list, right_list):
        if len(left_list) != len(right_list):
            raise ValueError("Both lists must be of the same length.")

        total_sum = sum(abs(a - b) for a, b in zip(left_list, right_list))
        return total_sum

    def solve(self, file_path):
        left_list, right_list = self._parse_input(file_path)
        return self._sum_of_absolute_differences(left_list, right_list)

file_path = "input.txt"
print(Solution().solve(file_path))

    
