from collections import Counter

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

    def _count_occurrences(self, right_list):
        return dict(Counter(right_list))

    def _compute_similarity_score(self, left_list, right_occurrence_dict):
        similarity_score = 0
        for value in left_list:
            similarity_score += right_occurrence_dict.get(value, 0)*value
        return similarity_score

    def solve(self, file_path):
        left_list, right_list = self._parse_input(file_path)
        right_occurrence_dict = self._count_occurrences(right_list)
        similarity_score = self._compute_similarity_score(left_list, right_occurrence_dict)
        return similarity_score
        
file_path = "input.txt"
print(Solution().solve(file_path))