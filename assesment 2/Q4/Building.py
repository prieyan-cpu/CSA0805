import time

def build_plus(parts):
    text = ""

    for p in parts:
        text += p + ";"

    return text


def build_join(parts):
    return "".join(p + ";" for p in parts)


def build_fstring(parts):
    return "".join(f"{p};" for p in parts)


sizes = [1000, 10000, 200000]

for size in sizes:
    items = [f"Item{i}:Rs{i % 50}" for i in range(size)]

    print("\nNumber of items:", size)

    results = {}

    for name, function in [
        ("Plus", build_plus),
        ("Join", build_join),
        ("F-string", build_fstring)
    ]:
        times = []

        for run in range(3):
            start = time.perf_counter()
            result = function(items)
            elapsed = time.perf_counter() - start
            times.append(elapsed)

        average = sum(times) / 3
        results[name] = result

        print(name, "times:", [round(t, 4) for t in times])
        print(name, "average:", round(average, 4), "seconds")

    print("Same text:", results["Plus"] == results["Join"] == results["F-string"])