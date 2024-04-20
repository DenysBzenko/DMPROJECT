import random

def randomMatrix(n, delta, directed=False):
    max_edges = n * (n - 1) / 2 if not directed else n * (n - 1)
    num_edges = int(max_edges * delta)

    # Створюємо матрицю суміжності розміром n x n
    adjacency_matrix = [[0] * n for _ in range(n)]

    # Генеруємо ребра
    edges = set()
    while len(edges) < num_edges:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i != j and (i, j) not in edges and (j, i) not in edges:
            edges.add((i, j) if directed else (min(i, j), max(i, j)))
            weight = random.randint(1, 10)  # Ваги ребер від 1 до 10
            adjacency_matrix[i][j] = weight
            if not directed:
                adjacency_matrix[j][i] = weight

    return adjacency_matrix
