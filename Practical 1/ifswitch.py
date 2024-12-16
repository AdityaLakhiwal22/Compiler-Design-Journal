#Craete a python code to check whether a text file have if else or switch statement present in it
import re

def check_if_else_and_switch_statements(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Regular expression pattern for detecting 'if-elif-else' chains
        if_else_pattern = r'\bif\s.*:\n( {4}.*\n)*(?: {4}elif\s.*:\n( {4}.*\n)*|\belse\s*:.*\n( {4}.*\n)*)?'

        # Regular expression pattern for detecting 'switch' statement with 'case' and 'default'
        switch_pattern = r'\bswitch\s*\([^\)]*\)\s*{\s*(?:\s*\bcase\s*[^:]+:\s*[^}]*\bbreak\s*;\s*)+(?:\s*\bdefault\s*:.*)?\s*}'

        # Check for 'if-else' statements
        if_else_found = re.search(if_else_pattern, content)
        # Check for 'switch' statement
        switch_found = re.search(switch_pattern, content, re.DOTALL)

        if if_else_found and switch_found:
            return "The file contains both 'if-else' statements and a 'switch' statement."
        elif if_else_found:
            return "The file contains 'if-else' statements."
        elif switch_found:
            return "The file contains a 'switch' statement."
        else:
            return "The file contains neither 'if-else' nor 'switch' statements."

    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

# Example usage
filename = input("Enter the path to the text file: ")
result = check_if_else_and_switch_statements(filename)
print(result)
