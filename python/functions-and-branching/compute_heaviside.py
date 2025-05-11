def compute_heaviside(position):
    return 1 if position >= 0 else 0

def test_heaviside():
    test_values = [-10, -10 - 15, 0, 10 - 15, 10]
    print("Testing compute_heaviside:")
    for x in test_values:
        h = compute_heaviside(x)
        print(f"H({x}) = {h}")

if __name__ == "__main__":
    test_heaviside()