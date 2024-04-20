# main.py

import numpy as np
import time
from algorithm import method_by_branches
from randomMatrix import generate_random_weighted_graph

n = 100  # Кількість вершин
density = 0.1  # Щільність (відношення кількості ребер до максимально можливої)

# Генеруємо випадковий зважений граф
adj_matrix = generate_random_weighted_graph(n, density)

main_matrix = np.array(adj_matrix)

start = time.time()

optimal_path = method_by_branches(main_matrix)

end = time.time()

execution_time = end - start

print(optimal_path)
print("Час виконання: ", execution_time)
