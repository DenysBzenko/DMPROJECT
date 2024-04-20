import numpy as np
import random

def generate_random_weighted_graph(n, density, is_undirected=True):

    max_edges_undirected = n * (n - 1) // 2



    if density <= 0:
        m = 0
    elif density >= 1:
        m = max_edges_undirected if max_edges_undirected > 0 else 0
    else:
        m = int(density * max_edges_undirected)


    adjacency_matrix = np.zeros((n, n), dtype=int)

    edges_generated = 0
    while edges_generated < m:

        u, v = random.randint(0, n-1), random.randint(0, n-1)
        if u != v and adjacency_matrix[u, v] == 0:

            weight = random.randint(1, 50)
            adjacency_matrix[u, v] = weight
            edges_generated += 1


            if not is_undirected:
                reverse_weight = random.randint(1, 50)
                adjacency_matrix[v, u] = reverse_weight

    return adjacency_matrix


n = 15
density = 0.5
adj_matrix = generate_random_weighted_graph(n, density, is_undirected=True)
print(adj_matrix)
