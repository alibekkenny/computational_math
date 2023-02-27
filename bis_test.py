import math


def getResult(x):
    return math.cos(x)-x*math.e**x


print("%.6f" % getResult(0.517578))
