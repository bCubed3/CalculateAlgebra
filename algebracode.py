# Algebra Calculator Code
import re

# function to solve equations

def solve_equation(equ):
    # x = c
    if(re.search(r"^[a-z] = \d+\.?\d*$", user_input)):
        return re.search(r"^[a-z]", user_input).group() + " = " + re.search(r"\d+\.?\d*", user_input).group()
    # (ax + b) = 0
    elif(re.search(r"^\(?[\+\-]?\d*[a-z] [\+\-] \d+\)? = 0$", user_input)):
        return "test 0"
    elif(re.search(r"^\d+[a-z] = [\+\-]?\d+$", user_input)):
        return "test 2"
    # (ax + b)(cx + d) = 0
    elif(re.search(r"^\([\+\-]?\d*[a-z] [\+\-] \d+\)\([\+\-]?\d*[a-z] [\+\-] \d+\) = 0$", user_input)):
        #solve_equation(re.search(r"^\([\+\-]?\d*[a-z] [\+\-] \d+\)", user_input).group() + " = 0")
        return "test 1"
    
    else:
        return "There has been an error."

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
