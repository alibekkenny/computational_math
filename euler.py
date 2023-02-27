# function to find result of f(x,y)
def getResult(x, y):
    return x+y


# euler method - approximate the curve of the solution by the tangent in each interval
def euler(x0, y0, xn, n):

    # Calculating step size
    h = (xn-x0)/n

    print('x0\ty0\tf(x,y)\tyn')
    for i in range(n):
        # get result of f(x,y)
        fxy = getResult(x0, y0)
        # find new yn based on previous value
        yn = y0 + h * fxy
        # print results correct to 4 digits after ,
        print('%.4f\t%.4f\t%0.4f\t%.4f' % (x0, y0, fxy, yn))
        # refresh results of values for the next calculations
        y0 = yn
        x0 = x0+h
    # print result after n steps, correct to 6 digits after ,
    print('\nResults: x=%.6f, y=%.6f' % (xn, yn))


# Input starting(initial) values
print('Enter start values:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
xn = float(input('xn = '))
step = int(input('Number of steps = '))

euler(x0, y0, xn, step)
