rain_falls = []
NUMBER_OF_MONTHS = 12
for i in range(NUMBER_OF_MONTHS):
    rain_falls.append(int(input(f'Enter rainfall for month {i+1}: ')))

total_rainfall = 0
for i in rain_falls:
    total_rainfall += i

print(f'The total rainfall for the year is {total_rainfall}')

average_rainfall = total_rainfall / NUMBER_OF_MONTHS

print(f'The average rainfall for the year is {average_rainfall}')

min = rain_falls[0]
for i in rain_falls:
    if i < min:
        min = i

max = rain_falls[0]
for i in rain_falls:
    if i > max:
        max = i

print(f'The minimum rainfall is month {min} and the maximum is month {max}.')


#print(rain_falls)