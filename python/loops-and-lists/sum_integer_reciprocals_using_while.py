# summation = 0
# starting_index = 1
# index = starting_index
# maximum_index = 100

# while index < maximum_index:
    # summation += 1 / index

# print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

def compute_reciprocal_sum(k_max):
    summation = 0.0
    index = 1
    while index <= k_max:
        summation += 1.0 / index
        index += 1
    return summation

for k_max in (3, 100):
    result = compute_reciprocal_sum(k_max)
    print(f"sum(k = 1 to {k_max}) 1/k = {result:.6f}")

# Method 1
# k needs to be defined
# Index needs to go up by 1 in the loop

# Method 2
# k(3) = 1 + 1/2 + 1/3 = 1.833
# Code result = 1.833333

# Method 3
# LLM Used: Gemini 2.0 Flash
# Output:

# It looks like the provided Python code has a few errors that prevent it from correctly calculating the sum \sum_{k=1}^{k_{max}} \frac{1}{k}. Let's break down the issues:
# Incorrect Loop Condition: The while loop condition is while index < maximum_index:. This means the loop will stop before the index reaches the maximum_index. To include the term where k equals maximum_index (which is 100 in this case), the condition should be while index <= maximum_index:.
# Missing Index Increment: Inside the while loop, the value of index is never updated. This means the loop will run indefinitely, always using the initial value of index (which is 1), leading to an infinite loop and an incorrect summation. You need to increment index in each iteration of the loop, typically with index += 1.
# Integer Division: The line summation += 1/index performs integer division if both 1 and index are treated as integers. This will result in 1/index being 0 for all index > 1. To perform floating-point division and get the correct fractional values, at least one of the operands should be a float. You can achieve this by writing 1.0/index or casting index to a float: summation += 1 / float(index).
# Here's the corrected code:
# summation = 0
# starting_index = 1
# index = starting_index
# maximum_index = 100

# while index <= maximum_index:
#     summation += 1.0 / index
#     index += 1

# print(f"sum(k={starting_index} to {maximum_index}) 1/k = {summation}")


# In summary, the three errors are:
# Incorrect loop condition: Should be <= instead of <.
# Missing index increment: The index variable needs to be incremented within the loop.
# Integer division: Ensure floating-point division by using 1.0 or casting index to a float.