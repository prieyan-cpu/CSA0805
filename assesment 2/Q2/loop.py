correct_otp = "1234"


def while_verification():
    attempts = 0

    while attempts < 3:
        otp = input("Enter OTP: ")

        if otp == "":
            print("Blank entry. Try again.")
            continue

        attempts += 1

        if otp == correct_otp:
            print("OTP verified successfully.")
            break
        else:
            print("Wrong OTP.")

    else:
        print("Account locked for 30 minutes.")


def for_verification():
    for attempts in range(3):
        otp = input("Enter OTP: ")

        if otp == "":
            print("Blank entry. Try again.")
            continue

        if otp == correct_otp:
            print("OTP verified successfully.")
            break
        else:
            print("Wrong OTP.")

    else:
        print("Account locked for 30 minutes.")


def security_verification():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        otp = input("Enter OTP: ")

        if otp == "":
            print("Blank entry.")
            continue

        attempts += 1

        if otp == correct_otp:
            print("OTP verified.")
            return

        print("Wrong OTP.")

    answer = input("Answer security question correctly? (yes/no): ")

    if answer.lower() == "yes":
        max_attempts += 2

        while attempts < max_attempts:
            otp = input("Enter OTP: ")

            if otp == "":
                continue

            attempts += 1

            if otp == correct_otp:
                print("OTP verified.")
                return

            print("Wrong OTP.")

    print("Account locked for 30 minutes.")


while_verification()