import random
import array as arr

def linear_regression(m, b, x, y):
    learn_rate = 0.01
    m += (learn_rate*(y-(m*x+b))*x)
    b += (learn_rate*(y-(m*x+b)))
    return m, b

x = arr.array('b', [1, 2, 3, 4])
y = arr.array('b', [1, 2, 3, 4])
m = 1
b = 1

epoch = 1000
for i in range(0, epoch):
    r = random.randint(0,3)
    m, b = linear_regression(m, b, x[r], y[r])

print("y = " + str(m)+"x + " + str(b))