
import numpy as np

n = int(input('Enter number of data points: '))


x = np.zeros((n))
y = np.zeros((n))


print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))


xp = float(input('Enter interpolation point: '))

yp = 0

for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

print('Interpolated value at %.3f is %.3f.' % (xp, yp))




# x[0]=5
# y[0]=150
# x[1]=7
# y[1]=392
# x[2]=11
# y[2]=1452
# x[3]=13
# y[3]=2366
# x[4]=17
# y[4]=5202