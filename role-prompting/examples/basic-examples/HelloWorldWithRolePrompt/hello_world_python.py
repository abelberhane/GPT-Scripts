# Role-prompt: Write a memory-efficient "Hello, World!" program in Python that's easy for beginners to understand.

def main():
    # Using a main function as it's a good practice, making the code more organized and readable for beginners.
    message = "Hello, World!"  # Storing the string in a variable to avoid magic values, which can be confusing for beginners.
    print(message)  # Print the message to the console.

# Check if the script is being run as the main module and, if so, call the main function.
# This is a common best practice that new Python learners should get used to seeing.
if __name__ == "__main__":
    main()
