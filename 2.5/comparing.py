"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# September 29, 2025
# Evan Chan
# Counting Bot

"""
Design Phase:
An algorithm that can track the amount of votes each option
in a user inputed category got, and then display them as well as
the most and least popular options.

1. Ask the user for input on a category to choose from, if an unknown number given, ask them to restart
2. Loop though every line in the file
3. Add up the totals of every option
4. Find the most and least popular options of a category
5. Print out the totals as well as the most and least popular options

"""
file = open("2.4/responses.csv")
file.readline()

# Give the user categories to choose from
print("Pick a category to analyze:")
print("2: Favourite digit")
print("3: Favourite pet")
print("4: Favourite subject")
print("5: Favourite sport to play")
print("6: Favourite sport to watch")
print("7: Favourite music genre")
print("8: Favourite movie genre")
print("9: Favourite fast food place")

# Ask the user for a category
category_choice = int(input("Enter the NUMBER of the category: ").strip(".,?!"))

# Laying down the conditions
if category_choice == 2 or category_choice == 3 or category_choice == 4 or category_choice == 5 or category_choice == 6 or category_choice == 7 or category_choice == 8 or category_choice == 9:

    answer_counts = {}
    
    # Loop through each line in the file
    for line in file:
        parts = line.strip().split(",")
        answer = parts[category_choice]
        
        # Adding the totals of each option
        if answer in answer_counts:
            answer_counts[answer] += 1
        else:
            answer_counts[answer] = 1


    # Finding the most and least popular options
    for first_answer in answer_counts:
        most_popular = first_answer
        least_popular = first_answer
        break  

    # Compare each answer to find most and least popular
    for option in answer_counts:
        if answer_counts[option] > answer_counts[most_popular]:
            most_popular = option
        if answer_counts[option] < answer_counts[least_popular]:
            least_popular = option

    # Print results
    print("\nResults:")
    for option in answer_counts:
        print(option + " : " + str(answer_counts[option]))

    print("\nMost popular: " + most_popular + " with " + str(answer_counts[most_popular]) + " votes")
    print("Least popular: " + least_popular + " with " + str(answer_counts[least_popular]) + " votes")
else:
    print("Invalid Number. Please try again")