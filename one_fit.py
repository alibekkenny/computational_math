import numpy as np
import matplotlib.pyplot as plt


def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    results["polynomial"] = coeffs.tolist()
    # r-squared
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y) / len(y)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)
    results["determination"] = ssreg / sstot
    return results


x = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
y = np.array([10, 18, 25, 29, 32, 20, 11, 5, 2, 0])

print(polyfit(x, y, 1))
