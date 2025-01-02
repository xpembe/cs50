vowels = ["a", "e", "i", "o", "u"]

text = input("Input: ").strip()

# Iterating over a text string
for letter in text:

    # Checking if letter in vowels
    if letter in vowels:
        text = text.replace(letter, "")

print(f"Output: {text}")
