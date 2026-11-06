from functools import lru_cache
import sys
import time

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


print("Answers from 1 to 6:")

for n in range(1, 7):
    print(n, "=", ways_memo(n))

print("\nFunction Call Comparison:")

for n in [10, 20, 25, 30]:
    calls = 0
    naive_result = ways_naive(n)
    naive_calls = calls

    calls = 0
    ways_memo.cache_clear()
    memo_result = ways_memo(n)
    memo_calls = calls

    print("\nn =", n)
    print("Naive:", naive_result, "Calls:", naive_calls)
    print("Memo:", memo_result, "Calls:", memo_calls)


print("\nCall Tree for n = 5")

print("""
ways(5)
├── ways(4)
│   ├── ways(3)
│   │   ├── ways(2)
│   │   └── ways(1)
│   └── ways(2)
└── ways(3)
    ├── ways(2)
    └── ways(1)
""")


print("Recursion Limit:", sys.getrecursionlimit())

ways_memo.cache_clear()

try:
    print("Memoised n=1000:", ways_memo(1000))
except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded")

start = time.perf_counter()
result = ways_loop(1000)
elapsed = time.perf_counter() - start

print("Iterative n=1000:", result)
print("Iterative time:", elapsed)