import math


def func(x):
    return (math.sin(x)-math.log(x)+math.exp(x))


# Function to perform calculations
def calculate(lower_limit, upper_limit, interval_limit):
    # 3rd order of polynomials can best be integrated using this rule (3/8)
    interval_size = (float(upper_limit - lower_limit) / interval_limit)
    sum = func(lower_limit) + func(upper_limit)

    # Calculates value till integral limit
    for i in range(1, interval_limit):
        if (i % 3 == 0):
            sum = sum + 2 * func(lower_limit + i * interval_size)
        else:
            sum = sum + 3 * func(lower_limit + i * interval_size)
    # gives exact value of the integral when integrand is a cubic
    return ((float(3 * interval_size) / 8) * sum)


# driver function
interval_limit = 6
lower_limit = 0.2
upper_limit = 1.4

integral_res = calculate(lower_limit, upper_limit, interval_limit)

# rounding the final answer to 6 decimal places
print(round(integral_res, 6))
