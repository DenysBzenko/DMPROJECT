
import time
from algorithm import method_by_branches
from randomMatrix import generate_random_weighted_graph , n , density


def print_path(method_name, path):
    if not path:
        print(f"Шлях не знайдено для методу {method_name}.")
    else:
        print(f"Найкоротший шлях методом {method_name}: {path}")
        print(f"Довжина шляху методом {method_name}: {len(path) - 1}")




adj_matrix = generate_random_weighted_graph(n, density)


start_bfs = time.time()
shortest_path_bfs, _ = method_by_branches(adj_matrix)
end_bfs = time.time()
execution_time_bfs = end_bfs - start_bfs


start_dfs = time.time()
_, shortest_path_dfs = method_by_branches(adj_matrix)
end_dfs = time.time()
execution_time_dfs = end_dfs - start_dfs


print("Час виконання алгоритму BFS:", execution_time_bfs)
print_path("BFS", shortest_path_bfs)

print("Час виконання алгоритму DFS:", execution_time_dfs)
print_path("DFS", shortest_path_dfs)
