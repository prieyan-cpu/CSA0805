
import copy
import sys
import time


# Original grid problem
rows, cols = 3, 4

bad = [[0] * cols] * rows

bad[0][1] = 7

# TODO 1: Correct grid using list comprehension
good = [[0 for j in range(cols)] for i in range(rows)]

good[0][1] = 7

print("bad:", bad)
print("good:", good)

print(bad[0] is bad[1], good[0] is good[1])


# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])


# List cannot be a dictionary key
try:
    test = {[13.0418, 80.2341]: "T Nagar"}
except TypeError as error:
    print("Error:", error)


# Aliasing
a = [10, 20, 30]
b = a

b[0] = 100

print("\nAliasing")
print("a:", a)
print("b:", b)
print("Same object:", a is b)


# Shallow copying
original = [[1, 2], [3, 4]]

shallow1 = copy.copy(original)
shallow2 = original[:]

shallow1[0][0] = 99

print("\nShallow copy")
print("Original:", original)
print("Shallow:", shallow1)


# Deep copying
original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 100

print("\nDeep copy")
print("Original:", original)
print("Deep:", deep)


# Function modifying list
def change_list(values):
    values.append(500)


numbers = [10, 20, 30]

change_list(numbers)

print("\nFunction result:", numbers)


# Tuple unpacking
coordinates = [
    (13.0827, 80.2707),
    (13.0418, 80.2341)
]

for latitude, longitude in coordinates:
    print("Latitude:", latitude, "Longitude:", longitude)


# Memory comparison
values = list(range(1000000))
tuple_values = tuple(values)

print("\nMemory comparison")
print("List memory:", sys.getsizeof(values))
print("Tuple memory:", sys.getsizeof(tuple_values))


# Tuple and list creation timing
start = time.perf_counter()
list_data = list(range(1000000))
list_time = time.perf_counter() - start

start = time.perf_counter()
tuple_data = tuple(range(1000000))
tuple_time = time.perf_counter() - start

print("\nCreation time")
print("List:", list_time)
print("Tuple:", tuple_time)


# Indexing time
start = time.perf_counter()

for i in range(100000):
    x = values[500]

list_index_time = time.perf_counter() - start

start = time.perf_counter()

for i in range(100000):
    x = tuple_values[500]

tuple_index_time = time.perf_counter() - start

print("List indexing:", list_index_time)
print("Tuple indexing:", tuple_index_time)


# List inside tuple
my_tuple = ([10, 20], [30, 40])

my_tuple[0].append(50)

print("\nTuple containing lists:", my_tuple)
