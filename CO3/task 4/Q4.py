
import timeit


ai_elective = {
    "192311001",
    "192311004",
    "192311007",
    "192311009"
}

iot_elective = {
    "192311002",
    "192311004",
    "192311009",
    "192311010"
}

all_students = set()

for i in range(1, 11):
    all_students.add("1923110" + str(i).zfill(2))


# TODO 1: Using set operators

both = ai_elective & iot_elective

exactly_one = ai_elective ^ iot_elective

neither = all_students - (ai_elective | iot_elective)


print("clash      :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither    :", sorted(neither))


# Rewriting using set methods

both_method = ai_elective.intersection(iot_elective)

exactly_one_method = ai_elective.symmetric_difference(iot_elective)

neither_method = all_students.difference(
    ai_elective.union(iot_elective)
)


print("\nUsing set methods")

print("clash:", sorted(both_method))
print("exactly one:", sorted(exactly_one_method))
print("neither:", sorted(neither_method))


# Remove duplicate registrations
registrations = [
    "192311001",
    "192311001",
    "192311004",
    "192311009",
    "192311004"
]

unique = set(registrations)

print("\nUnique registrations:", sorted(unique))


# Membership testing
sizes = [10000, 100000, 1000000]

for size in sizes:

    values = list(range(size))
    value_set = set(values)

    number = size - 1

    list_time = timeit.timeit(
        lambda: number in values,
        number=100
    )

    set_time = timeit.timeit(
        lambda: number in value_set,
        number=100
    )

    print("\nSize:", size)
    print("List membership:", list_time)
    print("Set membership:", set_time)


# Nested loop vs set intersection
list1 = list(range(1000))
list2 = list(range(500, 1500))

start = timeit.default_timer()

common = []

for x in list1:
    for y in list2:
        if x == y:
            common.append(x)

nested_time = timeit.default_timer() - start


start = timeit.default_timer()

common_set = set(list1) & set(list2)

set_time = timeit.default_timer() - start

print("\nNested loop time:", nested_time)
print("Set intersection time:", set_time)


# Edge cases
print("\nEmpty electives:", set() & set())

print("Identical electives:", ai_elective & ai_elective)


# Verify by hand
small_a = {1, 2, 3}
small_b = {2, 3, 4}

print("\nManual verification")
print("Both:", small_a & small_b)
print("Exactly one:", small_a ^ small_b)
print("Neither:", {1, 2, 3, 4, 5} - (small_a | small_b))
