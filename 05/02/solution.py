class Solution:

    def _parse_input(self, file_path):
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file]

        page_ordering_rules, updates = self._preprocess_input(lines)

        return page_ordering_rules, updates

    def _preprocess_input(self, lines):
        index = lines.index('')

        page_ordering_rules = lines[:index]
        page_ordering = {}
        for pair in page_ordering_rules:
            x, y = pair.split("|")
            x, y = int(x), int(y)
            if x not in page_ordering:
                page_ordering[x] = []
            page_ordering[x].append(y)

        updates = lines[index + 1:]
        updates = [update.split(",") for update in updates]

        return page_ordering, updates

    def _is_update_correct(self, page_ordering, update):
        is_correct = True
        update.reverse()
        for index, page in enumerate(update):
            previous_elements = update[index+1:]
            for element in previous_elements:
                if element in page_ordering[page]:
                    return False
        return True

    def _reorder_update(self, page_ordering, update):
        update.reverse()
        update_set = set(update)

        # Create a dependency graph based on page_ordering
        graph = {item: set() for item in update}
        for item, dependencies in page_ordering.items():
            if item in update:
                graph[item] = {dep for dep in dependencies if dep in update_set}

        # Perform topological sorting
        result = []
        visited = set()
        visiting = set()

        def visit(node):
            if node in visited:
                return
            if node in visiting:
                raise ValueError("Circular dependency detected!")
            visiting.add(node)
            for dep in graph[node]:
                visit(dep)
            visiting.remove(node)
            visited.add(node)
            result.append(node)

        for item in update:
            visit(item)

        return result
            
    def solve(self, file_path):
        page_ordering, updates = self._parse_input(file_path)
        total_middle_nums = 0
        for update in updates:
            update = [int(update) for update in update]
            if not self._is_update_correct(page_ordering, update):
                reordered_update = self._reorder_update(page_ordering, update)
                total_middle_nums += reordered_update[len(reordered_update) // 2]
        return total_middle_nums

file_path = "input.txt"
print(Solution().solve(file_path))