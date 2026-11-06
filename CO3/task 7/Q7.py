import re
import time


# Sample contacts from different phones
contacts = [

    {
        "name": "Dr. Ravi",
        "phones": ["+91 98400 12345"],
        "emails": ["ravi@gmail.com"]
    },

    {
        "name": "Ravi Kumar",
        "phones": ["9840012345"],
        "emails": ["ravi@yahoo.com"]
    },

    {
        "name": "Arun",
        "phones": ["+91 98765 43210"],
        "emails": ["arun@gmail.com"]
    },

    {
        "name": "Priya",
        "phones": ["9876543211"],
        "emails": []
    },

    {
        "name": "Ravi",
        "phones": ["9840012345", "9000011111"],
        "emails": ["ravi@gmail.com"]
    },

    {
        "name": "Unknown",
        "phones": [],
        "emails": ["unknown@gmail.com"]
    }

]


# Normalise phone numbers
def normalise_phone(phone):

    digits = re.sub(r"\D", "", phone)

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    elif len(digits) == 11 and digits.startswith("0"):
        digits = digits[1:]

    return digits


# Normalise names
def normalise_name(name):

    name = name.lower().strip()

    name = re.sub(
        r"^(dr|mr|mrs|ms)\.?\s+",
        "",
        name
    )

    name = re.sub(r"[^a-z ]", "", name)

    return name


# Contact merging
def merge_contacts(data):

    merged = {}
    phone_index = {}

    for i, contact in enumerate(data):

        name = contact.get("name", "").strip()

        names = set()

        if name:
            names.add(name)

        phones = set()

        for phone in contact.get("phones", []):

            number = normalise_phone(phone)

            if number:
                phones.add(number)

        emails = set()

        for email in contact.get("emails", []):

            email = email.strip().lower()

            if email:
                emails.add(email)

        # Find existing contact groups using phone numbers
        matched_keys = set()

        for phone in phones:

            if phone in phone_index:
                matched_keys.add(phone_index[phone])

        if len(matched_keys) == 0:

            # Missing phone numbers cannot identify duplicates
            if len(phones) > 0:
                key = sorted(phones)[0]
            else:
                key = "missing_" + str(i)

            merged[key] = {
                "names": set(),
                "phones": set(),
                "emails": set()
            }

        else:

            key = sorted(matched_keys)[0]

            # Combine multiple existing groups if necessary
            for other_key in matched_keys:

                if other_key != key and other_key in merged:

                    merged[key]["names"].update(
                        merged[other_key]["names"]
                    )

                    merged[key]["phones"].update(
                        merged[other_key]["phones"]
                    )

                    merged[key]["emails"].update(
                        merged[other_key]["emails"]
                    )

                    del merged[other_key]

        # Add new contact information
        merged[key]["names"].update(names)

        merged[key]["phones"].update(phones)

        merged[key]["emails"].update(emails)

        # Update phone index
        for phone in merged[key]["phones"]:
            phone_index[phone] = key

    return merged


# Execute merging
start = time.perf_counter()

result = merge_contacts(contacts)

execution_time = time.perf_counter() - start


# Display merged contacts
print("MERGED CONTACTS")

for key, details in result.items():

    print("\nContact ID:", key)

    print("Names:", sorted(details["names"]))

    print("Phone numbers:", sorted(details["phones"]))

    print("Emails:", sorted(details["emails"]))


print("\nTotal contacts:", len(result))

print("Execution time:", execution_time)


# Generate large contact datasets
def generate_contacts(size):

    data = []

    for i in range(size):

        number = "98400" + str(i % 50000).zfill(5)

        contact = {
            "name": "Person " + str(i),
            "phones": [number],
            "emails": ["person" + str(i) + "@gmail.com"]
        }

        data.append(contact)

    return data


# Performance measurement
sizes = [1000, 100000]

for size in sizes:

    test_data = generate_contacts(size)

    start = time.perf_counter()

    merged_data = merge_contacts(test_data)

    total_time = time.perf_counter() - start

    print("\nInput contacts:", size)

    print("Merged contacts:", len(merged_data))

    print("Execution time:", total_time)


# Missing field test
missing_contacts = [
    {
        "name": "Person A",
        "phones": [],
        "emails": ["a@gmail.com"]
    },

    {
        "name": "",
        "phones": ["9840012345"],
        "emails": []
    }
]

print("\nMissing field test:")

print(merge_contacts(missing_contacts))


# ---------- Alternative concept: pairwise comparison vs dictionary ----------
def pairwise_merge(data):
    n = len(data)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    numbers = [{normalise_phone(p) for p in c["phones"]} for c in data]

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] & numbers[j]:
                parent[find(i)] = find(j)

    return len({find(i) for i in range(n)})


print("\nPAIRWISE vs DICTIONARY")
print("%-10s %-15s %-15s" % ("n", "Pairwise (s)", "Dictionary (s)"))

for size in [1000, 2000, 5000]:
    test_data = generate_contacts(size)

    start = time.perf_counter()
    pairwise_merge(test_data)
    pair_time = time.perf_counter() - start

    start = time.perf_counter()
    merge_contacts(test_data)
    dict_time = time.perf_counter() - start

    print("%-10d %-15.4f %-15.4f" % (size, pair_time, dict_time))
