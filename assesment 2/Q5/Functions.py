def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


print("Buggy Function:")
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))

print("Default Values:", add_item_buggy.__defaults__)

print("\nCorrect Function:")

customer1 = add_item("Tea")
customer2 = add_item("Vada")
customer3 = add_item("Coffee")

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


def calculate_bill(amount, gst=5):
    tax = amount * gst / 100
    total = amount + tax

    return total, tax


total, gst = calculate_bill(200)

print("\nTotal Bill:", total)
print("GST:", gst)


college = "Saveetha"


def local_example():
    subject = "Python"
    print("Local:", subject)


def global_example():
    global college
    college = "Engineering"
    print("Global:", college)


def outer():
    message = "Hello"

    def inner():
        nonlocal message
        message = "Welcome"

    inner()
    print("Nonlocal:", message)


local_example()
global_example()
outer()

print("Final Global:", college)