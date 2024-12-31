def main():
    # Asking for a user to input something
    user_input = input()

    # Displaying the user input with actual emoji
    print(convert(user_input))


def convert(input):
    # replacing :) and :( emotions with 🙂 and 🙁 emoji respectively
    input = "🙂".join(input.split(":)"))
    input = "🙁".join(input.split(":("))
    return input


main()
