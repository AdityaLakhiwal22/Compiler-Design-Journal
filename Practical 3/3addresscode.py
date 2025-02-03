import re

class TACGenerator:
    def __init__(self):
        self.temp_count = 0

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

    def postfix_to_tac(self, postfix, target_variable):
        stack, tac_code = [], []
        for token in postfix:
            if token.isalnum():  # Operand (variable or constant)
                stack.append(token)
            else:  # Operator
                operand2, operand1 = stack.pop(), stack.pop()
                temp = self.generate_temp()
                tac_code.append(f"{temp} = {operand1} {token} {operand2}")
                stack.append(temp)
        tac_code.append(f"{target_variable} = {stack.pop()}")  # Final result assigned to target
        return tac_code

    def generate_tac(self, expression):
        target_variable = expression.split('=')[0].strip()
        postfix = self.infix_to_postfix(expression.split('=')[1].strip())  # Get postfix from the right side
        return self.postfix_to_tac(postfix, target_variable)


# Example Usage
def main():
    tac_gen = TACGenerator()
    expression = input("Enter an expression: ")
    tac_code = tac_gen.generate_tac(expression)
    
    print("Generated 3-address code:")
    print("\n".join(tac_code))

if __name__ == "__main__":
    main()
