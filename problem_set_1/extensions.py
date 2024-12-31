# Asking for a user to input filename
filename = input("File name: ")

# Split the name on every period
extension = filename.split(".")

# Checking for the extension of the file
if filename.endswith(
    (
        ".gif",
        ".jpg",
        ".jpeg",
        ".png",
    )
):
    print(f"image/{extension[-1]}")
elif "." in filename:
    print(f"Application/{extension[-1]}")
else:
    print("application/octet_stream")
