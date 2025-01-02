def main():
    # Asking the user for a camelCase variable input
    camel_case = input("camelCase: ").strip()

    snake_case = to_snake_case(camel_case)
    print("snake_case:", snake_case)


def to_snake_case(camel_case):
    for letter in camel_case:
        # Checking if there's an upper case letter
        if letter.isupper():
            # Taking the index of the upper case letter
            index = camel_case.index(letter)
            # Format the string to include the underscore before each uppercase letter
            camel_case = camel_case[:index] + "_" + camel_case[index:]
    return camel_case.lower()  # Convert the string to all lowercase


main()
