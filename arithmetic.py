def add(numList):
    if len(numList) == 1:
        return numList[0]
    else: 
        return (numList[0] + add(numList[1:]))

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return float(num1) / num2

def square(num1):
    return num1**2

def cube(num1):
    return num1**3

def power(num1, num2):
    return num1**num2

def mod(num1, num2):
    return num1%num2

