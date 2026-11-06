def normalise(text):
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()

    return text


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return (
        state.isalpha()
        and district.isdigit()
        and series.isalpha()
        and number.isdigit()
        and len(series) in (1, 2)
    )


def format_number(reg):
    if not is_valid(reg):
        return "Invalid Registration"

    return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


test_numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "mh 12 xyz 4567",
    "AP-39-C-1234"
]

for raw in test_numbers:
    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "valid")
        print("Receipt:", format_number(reg))
    else:
        print(raw, "->", reg, "INVALID")