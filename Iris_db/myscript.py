import math
def f(x):
    return x**4 - math.sin(x/4)

for i in range(1,4):
    print(f"f({i}) = {f(i)}")