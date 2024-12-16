#Create a text file containing if and else statement and create a python file to check whether the if else statement is present or valid is not
import re
def check_if_else_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Regular expression patterns for detecting if-else and elif blocks
        if_pattern = r'\bif\s.*:.*\n( {4}.*\n)*'   # Matches `if` with its block
        else_pattern = r'\belse\s*:.*\n( {4}.*\n)*'  # Matches `else` with its block
        elif_pattern = r'\belif\s.*:.*\n( {4}.*\n)*' # Matches `elif` with its block

        # Check for the presence of proper if-else or elif statements
        if_match = re.search(if_pattern, content)
        else_match = re.search(else_pattern, content)
        elif_match = re.search(elif_pattern, content)

        if if_match and else_match:
            return "The file contains proper 'if-else' statements."
        elif if_match:
            return "The file contains an 'if' statement but no 'else' statement."
        elif else_match:
            return "The file contains an 'else' statement but no 'if' statement."
        elif elif_match:
            return "The file contains an 'elif' statement."
        else:
            return "The file does not contain any proper 'if', 'else', or 'elif' statements."

    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

# Example usage
filename = input("Enter the path to the text file: ")
result = check_if_else_in_file(filename)
print(result)
