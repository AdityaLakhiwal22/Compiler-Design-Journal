def check_loops(filepath):
    try:
        with open(filepath, 'r') as file:
            text = file.read()
            # Patterns for loop types
            for_pattern = r"for\s+\w+\s+in\s+.+:"
            while_pattern = r"while\s+.+:"
            do_while_pattern = r"do\s*\{\s*(.*\s*)+?\}\s*while\s*\(\s*\w+\s*<\s*\d+\s*\)\s*;"


            # Check for each loop type
            has_for = re.search(for_pattern, text) is not None
            has_while = re.search(while_pattern, text) is not None
            has_do_while = re.search(do_while_pattern, text, re.MULTILINE) is not None

            return has_for, has_while, has_do_while

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return False, False, False
# Example usage

filepath = r"test.txt"
has_for, has_while, has_do_while = check_loops(filepath)

if has_for:
    print("The file contains 'for' loops.")
if has_while:
    print("The file contains 'while' loops.")
if has_do_while:
    print("The file contains 'do-while' loops.")
if not (has_for or has_while or has_do_while):
    print("The file does not contain any of the specified loop types.")