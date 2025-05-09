a = 1.0
b = 2.0
n = 20
h = (b - a) / n
x_for = []
for i in range(n + 1):
    x_for.append(round(a + i * h, 2))

x_comp = [round(a + i * h, 2) for i in range(n + 1)]
print(f"For x in [{a}, {b}] with {n} intervals, the interval length is h = {h:.3f}, and")
print("Using a for loop:")
print(f"x = {x_for}")
print("Using list comprehension:")
print(f"x = {x_comp}")