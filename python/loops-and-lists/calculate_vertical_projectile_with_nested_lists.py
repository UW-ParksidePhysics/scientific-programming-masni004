v0 = 10.00
g = 9.81
n = 8
t_max = 2 * v0 / g
h = t_max / n
times = [i * h for i in range(n + 1)]
positions = [v0 * t - 0.5 * g * t**2 for t in times]
times_positions = [times, positions]

print(f"For v₀ = {v0:.2f} m/s on Earth (g = {g:.2f} m/s²):")
print(f"{'t (s)':>7} {'y (m)':>9}")
print("-" * 17)

for i in range(len(times_positions[0])):
    for column in times_positions:
        print(f"{column[i]:7.2f}", end=" ")
    print()

print()
time_positions = list(zip(times, positions))
print("Same data, now stored as rows in time_positions:")
print(f"{'t (s)':>7} {'y (m)':>9}")
print("-" * 17)

for t, y in time_positions:
    print(f"{t:7.2f} {y:9.2f}")