"""
AUTHOR: Mary Grizelle Hamor
DESCRIPTION: This program is a simple command line calculator that solve for the mathematical expression entered by the user.
"""

def main():
    expression = input("Enter an expression:\n")

    postfix = to_postfix(expression)
    print(f"{expression} = " + str(calculate_postfix(postfix)))

# Converts the mathematical expression into its postfix notation
# Postfix - The operator is written after its operands
def to_postfix(expression):
        stack = []
        postfix = []

        # Operator precedence (PEMDAS)
        priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

        for character in expression:
            if character.isnumeric() == True:
                postfix.append(character)
            elif character=='(':
                stack.append('(')
            elif character==')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else: 
                if character != " ":
                    while stack and stack[-1] != '(' and priority[character] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    stack.append(character)

        while stack:
            postfix.append(stack.pop())

        return postfix

def calculate_postfix(postfix):
    stack = []
    value = 0
    count = 0

    operators = ['+', '-', '*', '/', '(', ')', '^']

    while count < len(postfix):
        if postfix[0] not in operators:
            stack.append(int(postfix.pop(0)))
        else:
            a = stack.pop()
            b = stack.pop()
            if postfix[0] == '*':
                stack.append(int(a) * int(b))
            elif postfix[0] == '+':
                stack.append(int(a) + int(b))
            elif postfix[0] == '^':
                stack.append(int(b) ** int(a))
            elif postfix[0] == '/':
                stack.append(int(b) / int(a))
            elif postfix[0] == '-':
                stack.append(int(b) - int(a))
            postfix.pop(0)

    value = stack.pop(0)
    return value

if __name__ == "__main__":
    main()