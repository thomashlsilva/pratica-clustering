import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial import distance

# create dataset
F = np.array([[7587, 321, 112, 950],
              [6695, 211, 345, 820],
              [3788, 308, 450, 750],
              [8108, 278, 88, 999],
              [5652, 223, 212, 812],
              [6777, 355, 90, 901],
              [5812, 401, 185, 788],
              [7432, 208, 208, 790]])

# Transpose matrix
Ft = np.zeros((len(F[0]), len(F)))
# Iterate through rows
for i in range(len(F)):
    # Iterate through columns
    for j in range(len(F[0])):
        Ft[j][i] = F[i][j]


# normalize function
def normalize(x):
    x_n = np.zeros(len(x))
    for i in range(len(x)):
        x_n[i] = (x[i] - x.min()) / (x.max() - x.min())
    return x_n


# create normalized matrix
Fn = np.zeros(Ft.shape)
for i in range(Ft.shape[0]):
    Fn[i] = normalize(Ft[i])

'''
# covariance matrix in hand
cov = np.cov(Fn, rowvar=False, bias=False)
cov_inv = np.linalg.inv(cov)

# mahalanobis distance calculation
dist = distance.pdist(Fn, 'mahalanobis', VI=None)
condensed_dist = distance.squareform(dist)
'''

linkage_method = 'single'    # 'single', 'complete', 'average', 'centroid', 'ward'
distance_metric = 'cosine'   # 'euclidean', 'cosine', 'correlation', 'chebyshev'

# clustering em cima das linhas, ou seja, das amostras
# igual livro Sueli nxp
linkage_matrix = hierarchy.linkage(Fn, linkage_method, metric=distance_metric, optimal_ordering=True)

# create dendrogram
dn = hierarchy.dendrogram(linkage_matrix, labels=["F1", "F2", "F3", "F4"])
plt.title("Single linkage - Cosine distance")
plt.show()
'''
1. Euclidean
2. Cosine
3. Correlation
4. Chebyshev
'''