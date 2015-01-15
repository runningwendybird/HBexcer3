# # No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read

from arithmetic import *

def main():

    while True:
        user_input = raw_input(">> ")
        tokens = user_input.split(" ")
        if tokens[0] =="q":
            break
        elif tokens[0] =="+":
            print (add(int(tokens[1]), int(tokens[2])))
        elif tokens[0] =="-":
            print (subtract(int(tokens[1]), int(tokens[2])))
        elif tokens[0] =="*":
            print (multiply(int(tokens[1]), int(tokens[2])))
        elif tokens[0] =="/":
            print (divide(int(tokens[1]), int(tokens[2])))
        elif tokens[0] =="square":
            print (square(int(tokens[1])))
        elif tokens[0] =="cube":
            print (cube(int(tokens[1])))
        elif tokens[0] =="pow":
            print (power(int(tokens[1]), int(tokens[2])))
        elif tokens[0] =="mod":
            print (mod(int(tokens[1]), int(tokens[2])))
        else:
            print "enter a valid input"

if __name__ == "__main__":
    main()



