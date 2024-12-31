# Asking for a user to input greeting
greeting = input("Greeting: ").strip()

# Checking if the user greet with hello or start with h or otherwise
if greeting.lower() == "hello":
    print("$0")
elif greeting[0].lower() == "h":
    print("$20")
else:
    print("$100")
