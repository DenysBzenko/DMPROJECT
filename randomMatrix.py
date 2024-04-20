import numpy as np
import random

def generate_random_weighted_graph(n, density, is_undirected=True):
    # Обчислюємо максимальну кількість ребер у звичайному та орієнтованому графах
    max_edges_undirected = n * (n - 1) // 2
    max_edges_directed = n * (n - 1)

    # Вираховуємо кількість ребер, які ми хочемо створити на основі заданої щільності
    if density <= 0:
        m = 0
    elif density >= 1:
        m = max_edges_undirected if max_edges_undirected > 0 else 0
    else:
        m = int(density * max_edges_undirected)

    # Створюємо пусту матрицю суміжності з випадковими вагами
    adjacency_matrix = np.zeros((n, n), dtype=int)

    edges_generated = 0
    while edges_generated < m:
        # Вибираємо випадкову пару вершин (u, v)
        u, v = random.randint(0, n-1), random.randint(0, n-1)
        if u != v and adjacency_matrix[u, v] == 0:
            # Встановлюємо випадкову вагу для ребра (u, v)
            weight = random.randint(1, 50)  # Змініть межі ваги за потребою
            adjacency_matrix[u, v] = weight
            edges_generated += 1

            # Якщо граф орієнтований і неорієнтований, можна також додати зворотнє ребро з випадковою вагою
            if not is_undirected:
                reverse_weight = random.randint(1, 50)  # Змініть межі ваги за потребою
                adjacency_matrix[v, u] = reverse_weight

    return adjacency_matrix

# Приклад використання:
n = 10  # Кількість вершин
density = 1  # Щільність (відношення кількості ребер до максимально можливої)
adj_matrix = generate_random_weighted_graph(n, density, is_undirected=True)
print(adj_matrix)
