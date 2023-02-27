import math

globalArr = []


# interpolation is the process of finding the most appropriate estimate for missing data
# forward used to extrapolate values of y to the left of the beginning which equals to interpolate near the beginning
def forward(arr):
    newArr = []
    for i in range(1, len(arr)):
        newArr.append(arr[i]-arr[i-1])
    globalArr.append(newArr[0])
    if len(newArr) > 1:
        # interpolation with unequal intervals, we can use lagranges interpolations to find derivative
        forward(newArr)
    else:
        return newArr


# this formula is used to extrapolate the value of y to the right
# interpolate the value of y is near the end of the set of values
def backward(arr):
    newArr = []
    for i in range(1, len(arr)):
        newArr.append(arr[i]-arr[i-1])
    globalArr.append(newArr[0])
    if len(newArr) > 1:
        forward(newArr)
    else:
        return newArr


def substituion(arr, n):
    substitution = arr[0]
    for i in range(1, len(arr)):
        nVal = 1
        for j in range(0, i):
            nVal *= (n-j)
        substitution += (arr[i]*nVal)/math.factorial(i)
    print("substitution: ", substitution)


# h = x1-x0
h = 0.001

# necessary to find f(2.75), so x = 2.75
# n = (x-x0)/h
n = (0.1604-0.160)/h

# array of values of y
arrY = [0.1593182066, 0.1603053541, 0.1612923412]
globalArr.append(arrY[0])


forward(arrY)
# print(globalArr)
substituion(globalArr, n)
