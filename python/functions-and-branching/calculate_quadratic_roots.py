import math
import cmath

def calculate_quadratic_roots(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        root_disc = math.sqrt(discriminant)
    else:
        root_disc = cmath.sqrt(discriminant)
    r1 = (-b + root_disc) / (2 * a)
    r2 = (-b - root_disc) / (2 * a)
    return r1, r2

def test_single_root():
    a, b, c = 1, 2, 1
    expected = (-1.0, -1.0)
    roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 +2x +1 = 0: expected roots = {expected[0]:.1f}, {expected[1]:.1f}")
    print(f"calculate_quadratic_roots(1, 2, 1) = {roots[0]:.1f}, {roots[1]:.1f}")
    print(f"types: {type(roots[0]).__name__}, {type(roots[1]).__name__}\n")

def test_roots_float():
    a, b, c = 1, -2, -3
    expected = (3.0, -1.0)
    roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 -2x -3 = 0: expected roots = {expected[0]:.1f}, {expected[1]:.1f}")
    print(f"calculate_quadratic_roots(1, -2, -3) = {roots[0]:.1f}, {roots[1]:.1f}")
    print(f"types: {type(roots[0]).__name__}, {type(roots[1]).__name__}\n")

def test_roots_complex():
    a, b, c = 1, 0, 1
    expected = (1j, -1j)
    roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 +0x +1 = 0: expected roots = {expected[0]}, {expected[1]}")
    print(f"calculate_quadratic_roots(1, 0, 1) = {roots[0]}, {roots[1]}")
    print(f"types: {type(roots[0]).__name__}, {type(roots[1]).__name__}\n")

if __name__ == "__main__":
    test_single_root()
    test_roots_float()
    test_roots_complex()