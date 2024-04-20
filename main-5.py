import numpy as np
import time

from algorithm import method_by_branches
from randomMatrix import randomMatrix

# Встановлюємо кількість вершин та щільність
n = 100  # Кількість вершин
delta = 0.1  # Щільність

# Викликаємо randomMatrix для генерації матриці суміжності
matrix = randomMatrix(n, delta)

main_matrix = np.array(matrix)

start = time.time()

# Виконуємо алгоритм на отриманій матриці
optimal_path = method_by_branches(main_matrix)

end = time.time()

execution = end - start

print(optimal_path)
print("time: ", execution)
