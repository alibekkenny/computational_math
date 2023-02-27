# obtaining result of f(x,y)
def getResult(x, y):
    return x+y


# to give some initial starting values will be useful Taylor series
def runge_kutta(x0, y0, xn, n):

    # Calculating step size
    h = (xn-x0)/n

    print('x0\ty0\tyn')
    for i in range(n):
        # Obtaining k values based on the runge kutta method formula k=hf(x0,y0)
        k1 = h * (getResult(x0, y0))
        k2 = h * (getResult((x0+h/2), (y0+k1/2)))
        k3 = h * (getResult((x0+h/2), (y0+k2/2)))
        k4 = h * (getResult((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        # Obtaining the result
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        y0 = yn
        x0 = x0+h
    # this rk method of second order is same as modified euler method
    print('\nResults: x=%.6f, y=%.6f' % (xn, yn))


# inputing starting values
# rounding errors may occur errors in performing numerical computation
print('Enter start values:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
xn = float(input('xn = '))
step = int(input('Number of steps = '))

runge_kutta(x0, y0, xn, step)
