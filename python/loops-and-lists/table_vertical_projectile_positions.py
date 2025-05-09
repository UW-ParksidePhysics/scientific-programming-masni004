v0 = 10.00
n = 8

bodies = [
    ("Earth", 9.81),
    ("Moon", 1.62),
]

line_width = 50

print(f"For initial velocity of {v0:.2f} m/s:")
print("-" * line_width)
for name, g in bodies:
    print(f"{name} (g = {g:.2f} m/s²)", end="   ")
print("\n" + "-" * line_width)

for _ in bodies:
    print(f"{'t (s)':>7} {'y (m)':>9}", end=" ")
print("\n" + "-" * line_width)

print("using a for loop:")
all_vals = []
for name, g in bodies:
    t_max = 2 * v0 / g
    h = t_max / n
    vals = [
        (i * h,
         v0 * (i * h) - 0.5 * g * (i * h) ** 2)
        for i in range(n + 1)
    ]
    all_vals.append(vals)

for i in range(n + 1):
    for vals in all_vals:
        t, y = vals[i]
        print(f"{t:7.3f} {y:9.3f}", end=" ")
    print()
print()


print("using a while loop:")
for name, g in bodies:
    print(f"{name} (g = {g:.2f} m/s²):")
    print(f"{'t (s)':>7} {'y (m)':>9}")
    t_max = 2 * v0 / g
    h = t_max / n
    i = 0
    while i <= n:
        t = i * h
        y = v0 * t - 0.5 * g * t ** 2
        print(f"{t:7.3f} {y:9.3f}")
        i += 1
    print()