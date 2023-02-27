import numpy as np
from numpy.linalg import eig


a = np.array([[8, -4, 2], 
              [4, 0, 2],
              [0, -2, -4]])
w,v=eig(a)
print('Eigen-value:', w)
print('Eigen-vector', v)