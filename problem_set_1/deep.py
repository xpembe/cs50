# Asking for a user for the answer
print("What is the Answer to the Great Question of Life the Universe, and Everything?")
answer = input().strip()

# Checking if the user input the correct answers
if answer == "42" or answer == "forty-two" or answer == "Forty Two":
    print("Yes")
else:
    print("No")