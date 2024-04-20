# algorithm.py

import numpy as np
from collections import deque

def method_by_branches(main_matrix):
    length = np.inf
    n = main_matrix.shape[0]
    min_cost = np.inf
    min_path = []

    def cost(path):
        total = 0
        for i in range(n-1):
            total += main_matrix[path[i], path[i+1]]
        total += main_matrix[path[-1], path[0]]
        return total

    def branch_and_bound(path, bound):
        nonlocal min_cost, min_path, length

        if len(path) == n:
            path_cost = cost(path)
            if path_cost < min_cost:
                min_cost = path_cost
                min_path = path
            length = min_cost
            return

        for i in range(n):
            if i not in path:
                new_bound = bound - main_matrix[path[-1], i]
                if new_bound < min_cost:
                    branch_and_bound(path + [i], new_bound)

    def bfs_shortest_path(adj_matrix, start, goal):
        queue = deque([(start, [start])])
        visited = set([start])

        while queue:
            node, path = queue.popleft()

            if node == goal:
                return path

            # Отримуємо індекси сусідів, які мають ненульові значення у матриці суміжності
            neighbors = np.nonzero(adj_matrix[node])[0]

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)

        return []  # Якщо шлях не знайдено

    def dfs_shortest_path(adj_matrix, start, goal):
        stack = [(start, [start])]
        visited = set([start])

        while stack:
            node, path = stack.pop()

            if node == goal:
                return path

            # Отримуємо індекси сусідів, які мають ненульові значення у матриці суміжності
            neighbors = np.nonzero(adj_matrix[node])[0]

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)

        return []  # Якщо шлях не знайдено

    # Виклик функції з пошуком найкоротшого шляху за допомогою BFS
    shortest_path_bfs = bfs_shortest_path(main_matrix, 0, n-1)

    # Виклик функції з пошуком найкоротшого шляху за допомогою DFS
    shortest_path_dfs = dfs_shortest_path(main_matrix, 0, n-1)

    return shortest_path_bfs, shortest_path_dfs


# Ви можете додати інші допоміжні функції або класи нижче, якщо потрібно
