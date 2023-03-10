import math


def f(x):
    return x*(math.e**x)

# Implementing trapezoidal method


def trapezoidal(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration = integration + 2 * f(k)

    # Finding final integration value
    integration = integration * h / 2

    # gives exact value of the integral when integrand is a linear
    return integration


# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = trapezoidal(lower_limit, upper_limit, sub_interval)

# Print result
print("Integration result by Trapezoidal method is: ", result)
