import time
import tracemalloc
import filecmp

items = [f"Item{i}:Rs{i % 50}" for i in range(200000)]


def original_program():
    text = ""

    for item in items:
        text += item + ";"

    with open("original_output.txt", "w") as file:
        file.write(text)


def redesigned_program():
    with open("redesigned_output.txt", "w") as file:
        for item in items:
            file.write(item + ";")


def measure(function):
    tracemalloc.start()

    start = time.perf_counter()
    function()
    elapsed = time.perf_counter() - start

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return elapsed, peak


original_time, original_memory = measure(original_program)

redesign_time, redesign_memory = measure(redesigned_program)

print("ORIGINAL PROGRAM")
print("Execution Time:", round(original_time, 4), "seconds")
print("Peak Memory:", original_memory, "bytes")

print("\nREDESIGNED PROGRAM")
print("Execution Time:", round(redesign_time, 4), "seconds")
print("Peak Memory:", redesign_memory, "bytes")

print("\nVALIDATION")
print("Same Output:", filecmp.cmp(
    "original_output.txt",
    "redesigned_output.txt",
    shallow=False
))