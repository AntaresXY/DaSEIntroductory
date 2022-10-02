import random
import math

def f(x):
    return x **2 + 4 * x * math.sin(x)

S = (3.0 - 2.0) * 13
N = 10000000
C = 0
for i in range(N):
    x = random.uniform(2.0, 3.0)
    y = random.uniform(0.0, 13.0)
    if y <= f(x):
        C += 1
I = C * S / N
print(I)