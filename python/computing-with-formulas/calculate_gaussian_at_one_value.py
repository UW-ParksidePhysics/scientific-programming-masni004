import math

mean = 0
standard_deviation = 2
input_value = 1

coefficient = 1 / (standard_deviation * math.sqrt(2 * math.pi))
exponent = -((input_value - mean) ** 2) / (2 * standard_deviation ** 2)
gaussian_value = coefficient * math.exp(exponent)

print(f"Mean: {mean}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Input Value: {input_value}")
print(f"Gaussian Function Result: {gaussian_value:.5f}")