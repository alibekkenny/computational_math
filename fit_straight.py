import math
import numpy

lsm = dict()
lsm["x"] = 0
lsm["y"] = 0
lsm["x2"] = 0
lsm["x3"] = 0
lsm["x4"] = 0
lsm["xy"] = 0
lsm["x2y"] = 0

# curve fitting method -
# find equations of approximating curves which fit a given data


def getSums(xArr, yArr):

    for i in range(len(xArr)):
        lsm["x"] += xArr[i]
        lsm["y"] += yArr[i]
        lsm["x2"] += math.pow(xArr[i], 2)
        lsm["xy"] += xArr[i]*yArr[i]
        # lsm["x2y"] += math.pow(xArr[i], 2)*yArr[i]


def printSums(lsm):
    print("%f\t%f\t%f\t%f" % (
        lsm["x"], lsm["y"], lsm["x2"], lsm["xy"]))


xArr = [5, 10, 15]
yArr = [1.45, 1.18, 1]
getSums(xArr, yArr)

printSums(lsm)
# Sxy​=∑xy−n∑x∑y​
# sum(y) = an+b*sum(x)+c*sum(x2)
# sum(xy) = a*sum(x)+b*sum(x2)+c*sum(x3)
# sum(x2y) = a*sum(x2)+b*sum(x3)+c*sum(x4)
# print("%da+%db+%dc = %d" % (len(xArr), lsm["x"], lsm["x2"], lsm["y"]))
# print("%da+%db+%dc = %d" % (lsm["x"], lsm["x2"], lsm["x3"], lsm["xy"]))
# print("%da+%db+%dc = %d" % (lsm["x2"], lsm["x3"], lsm["x4"], lsm["x2y"]))

# a = numpy.array([[len(xArr), lsm["x"], lsm["x2"]],
#                  [lsm["x"], lsm["x2"], lsm["x3"]],
#                  [lsm["x2"], lsm["x3"], lsm["x4"]]])
# b = numpy.array([lsm["y"], lsm["xy"], lsm["x2y"]])


# x = numpy.linalg.solve(a, b)
# Sxx​=∑x2−n(∑x)2​
b = (lsm["xy"]-len(xArr)*lsm["x"]*lsm["y"])/(lsm["x2"]-len(xArr)*(lsm["x"]**2))
y = lsm["y"]/len(xArr)
x = lsm["x"]/len(xArr)
a = y-b*x
print("Y=%fa+%fb" % (a, b))
