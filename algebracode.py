# Algebra Calculator Code
import re

# function to solve equations

def solve_equation(equ):
    # x = c
    if(re.search(r"^[a-z] = \d+$", user_input)):
        return re.search(r"^[a-z]", user_input).group() + " = " + re.search(r"\d+", user_input).group()
    elif(re.search(r"^\([a-z] [\+\-] \d+\)\([a-z] [\+\-] \d+\) = 0$", user_input)):
        solve_equation(re.search(r"^\([a-z] [\+\-] \d+\)$", user_input).group()+ " = 0")
    else:
        print("There has been an error.")

print("Welcome to bCubed's Algebra Calculator.")

while True:
    user_input = input()

    # test if input is an equation or an expression

    if(user_input == "help"):
        print("Help page to come.")
    elif("=" in user_input):
        print(solve_equation(user_input))
    else:
        print("Expression")
