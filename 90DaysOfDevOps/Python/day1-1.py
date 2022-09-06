# env=input("enter the cloud platform:")


# if env== "aws" or env == "AWS" :
#     print("you are in aws environment")
# else:
#     print("you are not in aws but in another cloud")

from ast import operator
from doctest import OutputChecker


num1 = float(input("Enter num1:"))
num2 = float (input("Enter num2:"))

operator = input("Enter operator:")

if operator == "+":
    output=num1+num2

if operator == "-":
    output=num1-num2

if operator == "*":
    output=num1*num2

print("your calculation is: ",output)

if output < 3:
    print(output,"is less than 3")

elif output == 3:
    print(output," is equal to 3")

else:
    print(output," is greater than 3")