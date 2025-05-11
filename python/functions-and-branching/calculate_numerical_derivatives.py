import math

def calculate_difference_quotient(function, position, interval=1e-5):
    return (function(position + interval) - function(position - interval)) / (2 * interval)


def test_difference_quotient():
    def f(x): return 5 * (x * x) - 3 * x + 2
    def fprime(x): return 10 * x - 3

    for x in (0.0, 1.0, -2.0, 2.5):
        approx = calculate_difference_quotient(f, x)
        expected = fprime(x)
        assert math.isclose(approx, expected, abs_tol=0.0), (
            f"At x={x}, expected {expected}, got {approx}"
        )


def run_tests():
    h = 0.01
    tests = [
        ("eˣ",      math.exp,                    0.0,               math.exp(0.0)),
        ("e⁻²ˣ²",   lambda x: math.exp(-2 * x * x), 0.0,            0.0),
        ("cos(x)",  math.cos,                    2 * math.pi,      -math.sin(2 * math.pi)),
        ("ln(x)",   math.log,                    1.0,               1.0),
    ]
    print(f"{'Function':>8} {'x':>8} {'Exact':>12} {'Approx':>12} {'Error':>12}")
    print("-" * 56)
    for name, func, x, exact in tests:
        approx = calculate_difference_quotient(func, x, h)
        error = approx - exact
        print(f"{name:>8} {x:8.2f} {exact:12.6f} {approx:12.6f} {error:12.6f}")

if __name__ == "__main__":
    test_difference_quotient()
    run_tests()