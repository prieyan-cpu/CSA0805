
import time
import sys


# Railway timetable
timetable = {

    "12001": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai Central", "06:00", "06:05"),
            ("Katpadi", "08:00", "08:05"),
            ("Bangalore", "11:00", "11:10")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri"}
    },

    "12002": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai Central", "07:00", "07:10"),
            ("Salem", "10:00", "10:05"),
            ("Coimbatore", "12:00", "12:10")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },

    "12003": {
        "name": "Madurai Express",
        "stops": [
            ("Chennai Central", "08:00", "08:05"),
            ("Trichy", "12:00", "12:05"),
            ("Madurai", "14:00", "14:10")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },

    "12004": {
        "name": "Mysore Express",
        "stops": [
            ("Chennai Central", "09:00", "09:10"),
            ("Katpadi", "11:00", "11:05"),
            ("Mysore", "15:00", "15:10")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat"}
    },

    "12005": {
        "name": "Kerala Express",
        "stops": [
            ("Chennai Central", "10:00", "10:05"),
            ("Salem", "13:00", "13:05"),
            ("Ernakulam", "17:00", "17:10")
        ],
        "days": {"Sun", "Mon", "Wed"}
    }

}


# Display timetable
print("RAILWAY TIMETABLE")

for train_no, details in timetable.items():

    print("\nTrain:", train_no)
    print("Name:", details["name"])
    print("Running days:", details["days"])

    for station, arrival, departure in details["stops"]:

        print(station, arrival, departure)


# Find trains at a station on a given day
def find_trains(data, station, day):

    result = []

    for train_no, details in data.items():

        if day in details["days"]:

            for stop, arrival, departure in details["stops"]:

                if stop == station:

                    result.append(
                        (train_no, details["name"], arrival, departure)
                    )

    return result


station = "Chennai Central"
day = "Mon"

result = find_trains(timetable, station, day)

print("\nTrains at", station, "on", day)

for train in result:
    print(train)


# Sort trains by departure time
sorted_trains = sorted(
    result,
    key=lambda x: x[3]
)

print("\nSorted by departure time")

for train in sorted_trains:
    print(train)


# Create station index
def create_index(data):

    index = {}

    for train_no, details in data.items():

        for station, arrival, departure in details["stops"]:

            index.setdefault(station, []).append(
                (train_no, details["name"], departure,
                 details["days"])
            )

    return index


station_index = create_index(timetable)


# Search using station index
def indexed_search(index, station, day):

    result = []

    if station not in index:
        return result

    for train_no, name, departure, days in index[station]:

        if day in days:

            result.append(
                (train_no, name, departure)
            )

    return result


print("\nIndexed search")

print(indexed_search(
    station_index,
    "Chennai Central",
    "Mon"
))


# Compare query performance
start = time.perf_counter()

for i in range(1000):
    find_trains(timetable, "Salem", "Mon")

normal_time = time.perf_counter() - start


start = time.perf_counter()

for i in range(1000):
    indexed_search(station_index, "Salem", "Mon")

indexed_time = time.perf_counter() - start


print("\nQuery performance")
print("Normal search:", normal_time)
print("Indexed search:", indexed_time)


# Memory used by index
index_memory = sys.getsizeof(station_index)

for station, values in station_index.items():
    index_memory += sys.getsizeof(values)

print("\nIndex memory:", index_memory)


# Edge cases
print("\nUnknown station:",
      indexed_search(station_index, "Unknown", "Mon"))

print("Non-running day:",
      indexed_search(station_index, "Madurai", "Mon"))


# Nested structure access
print("\nThird station departure:",
      timetable["12001"]["stops"][2][2])
