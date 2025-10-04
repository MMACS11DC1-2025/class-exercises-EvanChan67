"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# September 29-October 5, 2025
# Evan Chan
# Counting Bot

"""
Design Phase:
First algorithm tracks the amount of votes each option
in a user inputed category got, and then display them as well as
the most and least popular options.
The second algorithm asks for a students name, and it tracks that students response
to the category, and compares it to the most popular option at the end

1. Ask the user for input on a category to choose from, if an unknown number given, ask them to restart
2. Ask the user for the name of a student within our class
3. Loop though every line in the file
4. Add up the totals of every option
5. Find the most and least popular options of a category
6. Print out the totals as well as the most and least popular options
7. Compares the student chosens response to the most popular response

"""

"""
TEST CASE 1: 7, Evan Chan

Pick a category to analyze:
2: Favourite digit
3: Favourite pet
4: Favourite subject
5: Favourite sport to play
6: Favourite sport to watch
7: Favourite music genre
8: Favourite movie genre
9: Favourite fast food place
Enter the NUMBER of the category: 7
Enter the full name of a student (e.g. Evan Chan): Evan Chan

Results:
Classical : 3
Hip-hop : 9
Pop : 6
Rock : 3
K-Pop : 4
Country : 1
Jazz : 1

Most popular: Hip-hop with 9 votes
Least popular: Country with 1 votes

Evan Chan's response of Hip-hop was the option with the most votes!
"""

"""
TEST CASE 2: 4, Steven Zhang

Pick a category to analyze:
2: Favourite digit
3: Favourite pet
4: Favourite subject
5: Favourite sport to play
6: Favourite sport to watch
7: Favourite music genre
8: Favourite movie genre
9: Favourite fast food place
Enter the NUMBER of the category: 4
Enter the full name of a student (e.g. Evan Chan): Steven Zhang

Results:
Math : 8
Science : 10
Social Studies : 1
French : 2
Physical Education : 3
Fine Arts : 2
English : 1

Most popular: Science with 10 votes
Least popular: Social Studies with 1 votes

It was fairly close! Steven Zhang's response of Math got 2 fewer votes than the most popular response, Science
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
category = int(input("Enter the NUMBER of the category: ").strip(".,?!"))

# Laying down the conditions
if 2 <= category <= 9:

    answer_counts = {}

    # Asking the user for the full name of a student in our class, and defining the variable for their answer
    student_name = input("Enter the full name of a student (e.g. Evan Chan): ").strip(".,?!")
    studentAnswer = None

    # Loop through each line in the file
    for line in file:
        parts = line.strip().split(",")

        # Identifies every name in the file
        name = parts[1].strip()
        answer = parts[category]
        
        # Adding the totals of each option
        if answer in answer_counts:
            answer_counts[answer] += 1
        else:
            answer_counts[answer] = 1

        # Pairing the name chosen with the names answer in the user specified category
        if name.lower() == student_name.lower():
            studentAnswer = answer

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
    
    # Check if student answer exists
    if studentAnswer is not None:

        # Case for if the students answer was the most popular
        if studentAnswer == most_popular:
            print("\n" + student_name + "'s response of " + studentAnswer +
                  " was the option with the most votes!")
        else:
            diff = answer_counts[most_popular] - answer_counts[studentAnswer]

            # Case for if the students answer was 1 less than the most popular
            if diff == 1:
                print("\nIt was super close! " + student_name + "'s response of " + studentAnswer +
                      " got " + str(diff) + " less vote than the most popular response, " +
                      most_popular)
                
            # Case for if the students answer was in between 2-4 less than the most popular
            elif 2 <= diff <5:
                print("\nIt was fairly close! " + student_name + "'s response of " + studentAnswer +
                      " got " + str(diff) + " fewer votes than the most popular response, " +
                      most_popular)
                
            # Case for if the students answer was 5 or more votes less than the most popular
            else:
                print("\nIt was not close at all! " + student_name + "'s response of " + studentAnswer +
                      " got " + str(diff) + " fewer votes than the most popular response, " +
                      most_popular)
                
    # If the student is not recognized
    else:
        print("Student could not be found.")

# If a response that was not an integer was inputted
else:
    print("Invalid response. Please try again")

