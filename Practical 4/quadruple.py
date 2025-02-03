import re

class QuadrupleGenerator:
    def __init__(self):
        self.temp_count = 0
        self.quadruples = []

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

    def postfix_to_quadruples(self, postfix):
        stack = []
        for token in postfix:
            if token.isalnum():  # Operand (variable or constant)
                stack.append(token)
            else:  # Operator
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.generate_temp()
                self.quadruples.append((result, token, operand1, operand2))
                stack.append(result)
        return stack[-1]  # The final result is the last element in the stack

    def generate_quadruples(self, expression):
        postfix = self.infix_to_postfix(expression.split('=')[1].strip())
        target_variable = expression.split('=')[0].strip()
        self.postfix_to_quadruples(postfix)
        # Add the final assignment to the target variable
        self.quadruples.append((target_variable, '=', self.quadruples[-1][0], ''))
        return self.quadruples


# Example Usage
def main():
    quad_gen = QuadrupleGenerator()
    expression = input("Enter an expression: ")
    quadruples = quad_gen.generate_quadruples(expression)
    
    # Printing Quadruples in a table format with headers
    print(f"{'Result':<10}{'Operator':<10}{'Operand1':<10}{'Operand2':<10}")
    print("="*40)
    for quad in quadruples:
        print(f"{quad[0]:<10}{quad[1]:<10}{quad[2]:<10}{quad[3]:<10}")

if __name__ == "__main__":
    main()
