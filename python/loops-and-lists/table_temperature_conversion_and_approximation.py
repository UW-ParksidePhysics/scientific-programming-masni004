maximum_temperature = 100
temperature = 0
ctemperature = 0
atemperature = 0
temperatures = []
ctemperatures = []
atemperatures = []
while temperature <= maximum_temperature:
    temperatures.append(temperature)
    ctemperature = (temperature - 32) * (5/9)
    ctemperatures.append(ctemperature)
    atemperature = (temperature - 30) * (1/2)
    atemperatures.append(atemperature)
    temperature += 10

print(temperatures)
print(ctemperatures)
print(atemperatures)