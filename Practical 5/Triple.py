import re

class TripleGenerator:
    def __init__(self):
        self.temp_count = 0
        self.triples = []

    def generate_temp(self):
        self.temp_count += 1
        return f"T{self.temp_count}"

    def precedence(self, op):
        return 1 if op in '+-' else 2 if op in '*/' else 0

    def infix_to_postfix(self, expression):
        operators, output = [], []
        for token in re.findall(r'[A-Za-z0-9_]+|[+\-*/^=()]', expression):
            if token.isalnum():  # Operand (variable or constant)
                output.append(token)
            elif token == '(':  # Left Parenthesis
                operators.append(token)
            elif token == ')':  # Right Parenthesis
                while operators[-1] != '(':  # Pop until '(' is encountered
                    output.append(operators.pop())
                operators.pop()  # Remove '('
            else:  # Operator
                while operators and self.precedence(operators[-1]) >= self.precedence(token):
                    output.append(operators.pop())
                operators.append(token)
        output.extend(reversed(operators))  # Pop all remaining operators
        return output

    def postfix_to_triples(self, postfix):
        stack = []
        for token in postfix:
            if token.isalnum():  # Operand (variable or constant)
                stack.append(token)
            else:  # Operator
                operand2 = stack.pop()
                operand1 = stack.pop()
                self.triples.append((token, operand1, operand2))
                stack.append(f"T{len(self.triples)}")  # Use the current index as the temporary result reference
        return stack[-1]  # The final result is the last element in the stack

    def generate_triples(self, expression):
        postfix = self.infix_to_postfix(expression.split('=')[1].strip())
        target_variable = expression.split('=')[0].strip()
        self.postfix_to_triples(postfix)
        # Add the final assignment to the target variable (without result in triples)
        self.triples.append(('=', self.triples[-1][2], '', target_variable))
        return self.triples


# Example Usage
def main():
    triple_gen = TripleGenerator()
    expression = input("Enter an expression: ")
    triples = triple_gen.generate_triples(expression)
    
    # Printing Triples in a table format with headers (without Result column)
    print(f"{'Operator':<10}{'Operand1':<10}{'Operand2':<10}")
    print("="*30)
    for triple in triples:
        print(f"{triple[0]:<10}{triple[1]:<10}{triple[2]:<10}")

if __name__ == "__main__":
    main()
