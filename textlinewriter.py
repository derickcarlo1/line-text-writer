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

    # Prompt the user to enter more lines of text or quit the program

            # If the user chooses to enter another line, call the line_writer function again
         
            # If the user chooses to quit, display a message indicating that the file is ready and exit the program
            
            # If the user enters an invalid choice, display an error message and prompt them again

# Call the main function to start the program
