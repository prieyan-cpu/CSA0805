
import random
import string
import time
from collections import Counter


calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}


# TODO 1: Word frequency using dictionary get()
def frequencies(texts, stop):

    counts = {}

    for sentence in texts:

        sentence = sentence.lower()

        for word in sentence.split():

            word = word.strip(string.punctuation)

            if word != "" and word not in stop:

                counts[word] = counts.get(word, 0) + 1

    return counts


# TODO 2: Top k words
def top(counts, k):

    result = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return result[:k]


result = frequencies(calls, STOP)

print("Word frequencies:", result)
print("Top words:", top(result, 3))


# Group complaints by district using setdefault()
complaints = [
    ("Chennai", "Seeds not received"),
    ("Madurai", "Fertiliser price high"),
    ("Chennai", "Water shortage"),
    ("Salem", "Crop damage"),
    ("Madurai", "Seeds delayed")
]

districts = {}

for district, complaint in complaints:

    districts.setdefault(district, []).append(complaint)

print("\nDistrict complaints:")

for district, values in districts.items():
    print(district, ":", values)


# Generate random complaints
templates = [
    "seeds delayed farmer subsidy",
    "fertiliser price increase",
    "water shortage crop damage",
    "seeds not received",
    "government subsidy delayed"
]

def generate_complaints(size):

    data = []

    for i in range(size):
        data.append(random.choice(templates))

    return data


# Compare dictionary, list.count and Counter
sizes = [1000, 10000, 100000]

for size in sizes:

    data = generate_complaints(size)

    words = []

    for sentence in data:
        words.extend(sentence.lower().split())

    # Dictionary method
    start = time.perf_counter()

    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    dict_time = time.perf_counter() - start

    # list.count method
    start = time.perf_counter()

    distinct = set(words)
    list_counts = {}

    for word in distinct:
        list_counts[word] = words.count(word)

    list_time = time.perf_counter() - start

    # Counter method
    start = time.perf_counter()

    counter_result = Counter(words)

    counter_time = time.perf_counter() - start

    print("\nComplaints:", size)
    print("Dictionary time:", dict_time)
    print("List count time:", list_time)
    print("Counter time:", counter_time)


# Edge cases
print("\nEmpty text:", frequencies([""], STOP))

print(
    "Case and punctuation:",
    frequencies(["SEEDS, seeds! Seeds."], STOP)
)
