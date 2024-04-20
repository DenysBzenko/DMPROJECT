# main.py

import numpy as np
import time
from algorithm import method_by_branches
from randomMatrix import generate_random_weighted_graph

# Функція для виведення шляху
def print_path(method_name, path):
    if not path:
        print(f"Шлях не знайдено для методу {method_name}.")
    else:
        print(f"Найкоротший шлях методом {method_name}: {path}")
        print(f"Довжина шляху методом {method_name}: {len(path) - 1}")  # Кількість ребер у шляху

# Параметри графа
n = 100  # Кількість вершин
density = 0.1  # Щільність (відношення кількості ребер до максимально можливої)

# Генеруємо випадковий зважений граф
adj_matrix = generate_random_weighted_graph(n, density)

start = time.time()

# Виклик функції з пошуком найкоротших шляхів за допомогою обох методів
shortest_path_bfs, shortest_path_dfs = method_by_branches(adj_matrix)

end = time.time()

execution_time = end - start

# Виводимо результати
print("Час виконання алгоритму:", execution_time)
print_path("BFS", shortest_path_bfs)
print_path("DFS", shortest_path_dfs)
