# Using the Hello World Example and Python Documentation. Il try grabbing 'Input' from user and personalise The new greeting.




# Create a greeting asking for user name and then store it into a variable called 'name'
name = input("What is your name ? ")

# Remove any Whitespace either side of the answer given by the user using the 'strip' method.
name = name.strip()

# Capitalize first letter of each name using 'title' method.
name = name.title()

# Print the 'name' Variable to screen within a message. The 'f' before the string tells Python to "Format" the varible into the print function to make it look english legable. The varible gets wraped in curly braces.
print(f"Hello {name}")

