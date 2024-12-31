def main():
    # Asking the user for the present time
    time = input("What time is it? ").strip()
    time = convert(time)

    # printing appropriate meal according to their time
    if 7.00 <= time <= 8.00:
        print("Breakfast time")
    if 12.00 <= time <= 13.00:
        print("Launch time")
    if 18.00 <= time <= 19.00:
        print("Dinner time")


# Convert the string time to a decimal number
def convert(time):
    time = float(time.replace(":", "."))
    return time


if __name__ == "__main__":
    main()
