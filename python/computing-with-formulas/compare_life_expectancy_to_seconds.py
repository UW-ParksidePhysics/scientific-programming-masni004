life = 77.5
life_in_seconds = life * 365 * 24 * 60 * 60
life_expectancy = 1000000000
print(f"CDC life expectancy is {life_in_seconds:.0f} seconds; {'yes' if life_in_seconds > life_expectancy else 'no'}, the CDC lifespan {'is' if life_in_seconds > life_expectancy else 'is not'} longer than 1 billion seconds.")