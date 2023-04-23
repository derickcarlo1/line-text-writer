# Import necessary libraries

# Define a function that writes multiple lines of text to a file named mylife.txt
def line_writer():
    # Open the file in append mode to allow writing new lines to it without deleting previous ones
    with open("mylife.txt", "a") as myfile:

       # Prompt the user to enter a line of text
        user_input = input("Enter a line of text: ")
        # Write the user's input to the file
        myfile.write(user_input + "\n")

# Define the main function that will be executed when the program is run
def main():
    # Display a header for the program
    print("=== Text Line Writer ===")
    print("Created by: Derick Carlo S. Herrera")
    print("=" * 25)

     # Call the line_writer function to write the first line of text to the file
    line_writer()

     # Prompt the user to enter more lines of text or quit the program
    while True:
        user_choice = input("Do you wish to add another line? (y/n): ")
        if user_choice.lower() == "y":
            # If the user chooses to enter another line, call the line_writer function again
            line_writer()
        elif user_choice.lower() == "n":
            # If the user chooses to quit, display a message indicating that the file is ready and exit the program
            print("Your file is ready! Thank you for using Text Line Writer.")
            break
        else:
            # If the user enters an invalid choice, display an error message and prompt them again
            print("Invalid choice. Please enter 'y' or 'n'.")

# Call the main function to start the program
