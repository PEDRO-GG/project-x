from sympy import sympify, symbols

# Get user input for a mathematical expression
user_input = input("Enter a mathematical expression: ")

# Convert the user input into a SymPy expression
expression = sympify(user_input)

# Identify the variables in the expression
variables = expression.free_symbols

# Display the identified variables
print("Variables in the expression:", variables)
