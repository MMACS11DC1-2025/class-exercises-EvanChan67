"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
#Evan Chan
#Calculator
#Sept 22

print("Input two integers:")
number1 = int(input())
number2 = int(input())

print("Now give me an operation:")
operation = input()
operationlist = ["+", "/", "-", "*"]

if operation == "-":
    subtract = number1 - number2
    print(str(number1) + "-" + str(number2) + "=" + str(subtract))
elif operation == "+":
    add = number1 + number2
    print(str(number1) + "+" + str(number2) + "=" + str(add))
elif operation == "*":
    multiply = number1 * number2
    print(str(number1) + "*" + str(number2) + "=" + str(multiply))
elif operation == "/":
    divide = number1 / number2
    print(str(number1) + "/" + str(number2) + "=" + str(divide))
else:
    print("Not recognized operation, please restart")
