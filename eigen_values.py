import numpy as np


def eigen(A):
    tolerance = 1.0e-6  # set a tolerance level for checking if an eigenvalue is real

    def is_real(val):
        return abs(val.imag) < tolerance

    def normalize(vec):
        magnitude = sum(x**2 for x in vec)**0.5
        return [x/magnitude for x in vec]

    n = len(A)  # number of rows in A
    eigen_values = []  # list to store eigenvalues
    eigen_vectors = []  # list to store corresponding eigenvectors

    # Gaussian elimination to convert A to a upper triangular matrix
    for i in range(n-1):
        pivot = max(range(i, n), key=lambda j: abs(A[j][i]))
        if i != pivot:
            A[i], A[pivot] = A[pivot], A[i]
        for j in range(i+1, n):
            m = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= m * A[i][k]

    # Back substitution to find eigenvectors
    for i in range(n-1, -1, -1):
        eigen_val = A[i][i]
        eigen_vec = [0.0 for j in range(n)]
        eigen_vec[i] = 1.0

        for j in range(i):
            eigen_vec[j] = -A[j][i]

        eigen_vec = normalize(eigen_vec)

        if is_real(eigen_val):
            eigen_values.append(eigen_val.real)
            eigen_vectors.append(eigen_vec)
        else:
            eigen_values.append(eigen_val)
            eigen_vectors.append(eigen_vec)
            eigen_values.append(eigen_val.conjugate())
            eigen_vectors.append(eigen_vec)

    return eigen_values, eigen_vectors


mat = np.array([[2, -1, 0],
                [-1, 2, -1],
                [0, -1, 2]])
eigVal, eigVec = np.linalg.eig(mat)
print(eigVal)
# print(eigVec)
