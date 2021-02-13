'''

This file contains the functions that you need for completing this assignment. 

1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''
import math

def expression_1(x):
    x = float(input("Enter x: "))
    result = math.pow(x,3) - (2*x + math.pow(x,2)) - 100
    print(f"The result is {result}")

expression_1('x')

def expression_2(x, y):
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    result = (math.pow(x,4) / 2*y) - (3*x*y) + ((6*y) / (7*x))
    print(f"The result is {result}")

expression_2('x', 'y')


def expression_3(x, y):
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    result = (math.pow(x,3) + math.pow(y,2)) / (math.pow(x,2) - math.pow(y,3))
    print(f"The result is {result}")

expression_3('x' , 'y')


if __name__ == "__main__":
    pass