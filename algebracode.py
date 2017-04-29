# Algebra Calculator Code

print("Welcome to bCubed's Algebra Calculator.")

user_input = input()

# test if input is an equation or an expression

if(user_input == "help"):
    print("Help page to come.")
elif("=" in user_input):
    print("Equation")
else:
    print("Expression")
