"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""

print("Would you like a burger for $5 (Yes/No)")
answer1 = input().lower().strip(".!?")

print("Would you like fries for $3 (Yes/No)")
answer2 = input().lower().strip(".!?")

total = 0

if answer1 == "yes":
    total = total + 5
if answer2 == "yes":
    total = total + 3

total = total*1.14
print("Your total is $" + str(total))