# finding determinant of 2x2 matrix
def detOf2x(arr):
    return arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0]


# finding determinant of 3x3 matrix
def detOf3x(arr):
    return (arr[0][0]*arr[1][1]*arr[2][2]+arr[0][1]*arr[1][2]*arr[2][0]+arr[0][2]*arr[1][0]*arr[2][1])-(arr[2][0]*arr[1][1]*arr[0][2]+arr[2][1]*arr[1][2]*arr[0][0]+arr[2][2]*arr[1][0]*arr[0][1])


# multiply 2 matrices
# interpolation finding the best estimate for missing data
def multiplyMatrices(arr1, arr2):
    rows = len(arr1)
    cols = len(arr2[0])
    # creating empty matrix to store values of obatined product of matrices
    result = [[0 for rows in range(rows)] for cols in range(cols)]
    for i in range(len(arr1)):  # take each row from first matrix
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                # get results of row to column multiplication
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result
# to reverse
# print(np.linalg.inv(A))


# identical array
iArr = [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]]


arr = detOf3x([[8, -4, 2],
               [4, 0, 2],
               [0, -2, -4]])

print(arr)
