maximum_integer = 24
total = 0
for i in range(1, maximum_integer + 1):
    total += i
    formula = maximum_integer * (maximum_integer + 1) // 2


print(f"n = {maximum_integer}")
print(f"sum(1, n) = {total}")
print(f"n(n+1)/2 = {formula}")


