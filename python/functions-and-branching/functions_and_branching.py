import numpy as np
def calculate_quadratic_roots(a,b,c):
    a = 1
    b = 0
    c = 0
    root1 = (-b + np.lib.scimath.sqrt(b**2 - 4*a*c))/(2 * a)
    root2 = (-b - np.lib.scimath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(root1)
    print(root2)
calculate_quadratic_roots(1,0,0)