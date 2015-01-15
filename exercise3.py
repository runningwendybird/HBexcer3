
# import from py module in same folder
from arithmetic import *

def input_and_parameter_check():
    """Ask for user input, and confirms it has the correct number of parameters."""
    while True:
        user_input = raw_input(">> ")
        tokens = user_input.split(" ")
        correct_num_items = {"+":3,"-":3,"*":3,"/":3,"square":2,"cube":2,"pow":3,"mod":3, "q":1}
        if len(tokens) != correct_num_items[tokens[0]]:
            print "You entered the wrong number of parameters. Enter Again."
        else:
            return tokens

def use_arithmetic_functions(to_calculate):
    """Takes in the user input (parameters), calls the function, and provides the answer."""
    if to_calculate[0] =="+":
        print (add(float(to_calculate[1]), float(to_calculate[2])))
    elif to_calculate[0] =="-":
        print (subtract(float(to_calculate[1]), float(to_calculate[2])))
    elif to_calculate[0] =="*":
        print (multiply(float(tto_calculate[1]), float(to_calculate[2])))
    elif to_calculate[0] =="/":
        print (divide(float(to_calculate[1]), float(to_calculate[2])))
    elif to_calculate[0] =="square":
        print (square(float(to_calculate[1])))
    elif to_calculate[0] =="cube":
        print (cube(float(to_calculate[1])))
    elif to_calculate[0] =="pow":
        print (power(float(to_calculate[1]), float(to_calculate[2])))
    elif to_calculate[0] =="mod":
        print (mod(float(to_calculate[1]), float(to_calculate[2])))

def main():
    """calls to the function for user to enter input, allows for quitting, 
    nd recognizes invalid input (not a list of parameters)"""
    while True:
        try:
            input_for_arthimetic_funct = input_and_parameter_check()
            if input_for_arthimetic_funct[0] =="q":
                break
            else:
                use_arithmetic_functions(input_for_arthimetic_funct)
        except:
            print "enter a valid input"

if __name__ == "__main__":
    main()



