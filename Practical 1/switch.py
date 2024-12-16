import re

def check_switch_statement(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Regular expression pattern for detecting a 'switch' statement with 'case' and 'default'
        switch_pattern = r'\bswitch\s*\([^\)]*\)\s*{\s*(?:\s*\bcase\s*[^:]+:\s*[^}]*\bbreak\s*;\s*)+(?:\s*\bdefault\s*:.*)?\s*}'

        # Search for the pattern
        switch_found = re.search(switch_pattern, content, re.DOTALL)

        if switch_found:
            return "The file contains a valid 'switch' statement with cases and default."
        else:
            return "The file does not contain a valid 'switch' statement."

    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

# Example usage
filename = input("Enter the path to the text file: ")
result = check_switch_statement(filename)
print(result)
