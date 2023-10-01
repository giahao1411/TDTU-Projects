#bai 9 

import numpy as np

def cosine_similarity(matrix):
  prod = np.matmul(matrix, matrix.T)

  norm = np.sqrt(np.sum(matrix**2, axis = 1))

  outer_norm = np.outer(norm, norm)

  cosine_similarity_matrix = prod/outer_norm
  
  return cosine_similarity_matrix

A = np.array([
    [0, 4, 0, 0, 0, 2, 1, 3],
    [3, 1, 4, 3, 1, 2, 0, 1],
    [3, 0, 0, 0, 3, 0, 3, 0],
    [0, 1, 0, 3, 0, 0, 2, 0],
    [2, 2, 2, 3, 1, 4, 0, 2]
])

print("cosine similarity matrix = \n", cosine_similarity(A))