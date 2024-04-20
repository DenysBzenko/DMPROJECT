import numpy as np

def method_by_branches(main_matrix):
    n = main_matrix.shape[0]
    min_cost = np.inf
    min_path = []

    def cost(path):
        total = 0
        for i in range(len(path) - 1):
            total += main_matrix[path[i], path[i + 1]]
        total += main_matrix[path[-1], path[0]]  # Closing the loop
        return total

    # Stack-based DFS implementation
    def dfs_stack(start_point):
        nonlocal min_cost, min_path
        stack = [([start_point], 0)]

        while stack:
            current_path, current_cost = stack.pop()
            if len(current_path) == n:
                path_cost = cost(current_path)
                if path_cost < min_cost:
                    min_cost = path_cost
                    min_path = current_path[:]
                continue

            last = current_path[-1]
            for i in range(n):
                if i not in current_path and main_matrix[last, i] > 0:
                    new_cost = current_cost + main_matrix[last, i]
                    if new_cost < min_cost:
                        stack.append((current_path + [i], new_cost))

    for start_point in range(n):
        dfs_stack(start_point)
        if len(min_path) == n:
            break

    return min_path, min_cost
