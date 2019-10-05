from sklearn.neighbors import KDTree
import numpy as np

points = np.array([[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4], [1, 2], [2, 1]])
tree = KDTree(points, leaf_size=2)

nearest_dist, nearest_ind = tree.query(points, k=2)

i = int(0)

for dist in nearest_dist[:, 1]:
    min_dist = float(9999)
    if dist < min_dist:
        min_dist = dist
        min_nodes = nearest_ind[i]
    i += 1

print('The minimum distance is:')
print(min_dist)

print('Between the points', min_nodes[0], ' and ', min_nodes[1])
