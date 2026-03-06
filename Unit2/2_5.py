#Write a program to read a file and display its contents. At the end it shall also display no. of words available in file.


try:
    with open("2_1.py", "r") as file:
        content = file.read()
        
        # Display file contents
        print("File Contents:\n")
        print(content)
        
        # Count words
        words = content.split()
        word_count = len(words)
        
        print("\nTotal number of words:", word_count)

except FileNotFoundError:
    print("Error: File not found.")
