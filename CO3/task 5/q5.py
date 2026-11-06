
import random
import time
import sys


# Generate temperature readings
readings = []

for i in range(10000):
    readings.append(random.uniform(-60, 60))


# Method 1: For loop with append
def using_loop(data):

    celsius = []
    fahrenheit = []

    for value in data:

        if -50 <= value <= 50:

            celsius.append(value)

            f = (value * 9 / 5) + 32

            fahrenheit.append(f)

    return celsius, fahrenheit


# Method 2: List comprehension
def using_comprehension(data):

    celsius = [
        value for value in data
        if -50 <= value <= 50
    ]

    fahrenheit = [
        (value * 9 / 5) + 32
        for value in data
        if -50 <= value <= 50
    ]

    return celsius, fahrenheit


# Method 3: Map and filter with lambda
def using_map_filter(data):

    valid = list(
        filter(lambda x: -50 <= x <= 50, data)
    )

    fahrenheit = list(
        map(lambda x: (x * 9 / 5) + 32, valid)
    )

    return valid, fahrenheit


# Execute all three methods
loop_result = using_loop(readings)

comprehension_result = using_comprehension(readings)

map_result = using_map_filter(readings)


print("Loop result:", loop_result[0][:5])

print("Comprehension result:",
      comprehension_result[0][:5])

print("Map result:", map_result[0][:5])


# Verify results
print("\nVerification")

print(loop_result == comprehension_result)
print(comprehension_result == map_result)


# Alarm minutes
alarm_minutes = []

for index, value in enumerate(readings):

    if -50 <= value <= 50:

        if value < 2 or value > 8:

            alarm_minutes.append(index + 1)

print("\nAlarm minutes:", alarm_minutes)


# Dictionary comprehension
temperature_dictionary = {
    i + 1: value
    for i, value in enumerate(readings)
    if -50 <= value <= 50
}

print("Temperature dictionary:",
      list(temperature_dictionary.items())[:5])


# Set comprehension
valid_temperature_set = {
    value for value in readings
    if -50 <= value <= 50
}

print("Unique valid temperatures:",
      len(valid_temperature_set))


# Performance comparison
sizes = [10000, 100000, 1000000]

for size in sizes:

    data = []

    for i in range(size):
        data.append(random.uniform(-60, 60))

    start = time.perf_counter()
    using_loop(data)
    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    using_comprehension(data)
    comprehension_time = time.perf_counter() - start

    start = time.perf_counter()
    using_map_filter(data)
    map_time = time.perf_counter() - start

    print("\nSize:", size)
    print("Loop time:", loop_time)
    print("Comprehension time:", comprehension_time)
    print("Map filter time:", map_time)


# Memory comparison
values = [x for x in range(100000)]

generator = (x for x in range(100000))

print("\nMemory comparison")

print("List memory:", sys.getsizeof(values))

print("Generator memory:", sys.getsizeof(generator))


# All-valid and all-invalid tests
all_valid = [3, 4, 5, 6, 7]

all_invalid = [60, 70, -60, -80]

print("\nAll valid:", using_comprehension(all_valid))

print("All invalid:", using_comprehension(all_invalid))
