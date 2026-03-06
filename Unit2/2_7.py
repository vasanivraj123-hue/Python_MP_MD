#Write a program to copy a text file using file handling mechanism.
try:
    with open("source.txt", "r") as source:
        content = source.read()

    with open("destination.txt", "w") as destination:
        destination.write(content)

    print("File copied successfully.")

except FileNotFoundError:
    print("Error: Source file not found.")
except IOError:
    print("Error: File handling error occurred.")
