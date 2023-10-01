#bai 10 

import numpy as np

def retrieve_nearest_doc(q, doc_vector):
  similarities = np.matmul(doc_vector, q) / (np.linalg.norm(doc_vector, axis = 1) * np.linalg.norm(q))

  nearest_doc_index = np.argmax(similarities)

  return nearest_doc_index

vector = np.array([
    [1.0, 0.5, 0.3, 0, 0, 0],
    [0.5, 1.0, 0, 0, 0, 0],
    [0, 1.0, 0.8, 0.7, 0, 0],
    [0, 0.9, 1.0, 0.5, 0, 0],
    [0, 0, 0, 1.0, 0, 1.0],
    [0, 0, 0, 0, 0.7, 0],
    [0.5, 0, 0.7, 0, 0, 0.9],
    [0, 0.6, 0, 1.0, 0.3, 0.2]
])

q = np.array([0, 0, 0.7, 0.5, 0, 0.3])

print("The nearest document is D:", retrieve_nearest_doc(q, vector) + 1)