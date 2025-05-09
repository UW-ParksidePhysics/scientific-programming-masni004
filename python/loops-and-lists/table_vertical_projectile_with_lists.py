v0 = 10.00
g = 9.81
n = 8

t_max = 2 * v0 / g
h = t_max / n

times = [i * h for i in range(n + 1)]
positions = [v0 * t - 0.5 * g * t**2 for t in times]

print(f"For v₀ = {v0:.2f} m/s, g = {g:.2f} m/s²:")
print(f"{'t (s)':>7} {'y (m)':>9}")
print("-" * 17)
for t, y in zip(times, positions):
    print(f"{t:7.3f} {y:9.3f}")