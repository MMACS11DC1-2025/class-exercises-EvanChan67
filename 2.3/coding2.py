"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

j1 = float(input())
j2 = float(input())
j3 = float(input())
j4 = float(input())
j5 = float(input())

final = (j1 + j2 + j3 + j4 + j5)/5

print("Your olympic score is " + str(final))