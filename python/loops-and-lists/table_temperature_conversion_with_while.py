maximum_temperature = 100
temperature = 0
ctemperature = 0
temperatures = []
ctemperatures = []
while temperature <= maximum_temperature:
    temperatures.append(temperature)
    ctemperature = (temperature - 32) * (5/9)
    ctemperatures.append(ctemperature)
    temperature += 10

print(temperatures)
print(ctemperatures)