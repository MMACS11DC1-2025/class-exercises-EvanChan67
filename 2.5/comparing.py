"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# September 29-October 8, 2025
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
TEST CASE 1: 7, evan chan

Pick a category to analyze:
1: Favourite digit
2: Favourite pet
3: Favourite subject
4: Favourite sport to play
5: Favourite sport to watch
6: Favourite music genre
7: Favourite movie genre
8: Favourite fast food place
Enter the NUMBER of the category: 7
Enter the full name of a student (e.g. Evan Chan) who you believe chose the most popular answer : evan chan     
==========================================================================================================================

Number of Votes Each Response Received:

Fantasy/Sci-Fi : 6
Thriller/Mystery : 7
Comedy : 5
Superhero : 1
Horror : 3
Adventure : 4
Rom-com : 1

Most popular: Thriller/Mystery with 7 votes
Least popular: Superhero with 1 votes

Evan Chan chose Horror

It was fairly close! Evan Chan's response of Horror got 4 fewer votes than the most popular response, Thriller/Mystery
"""

"""
TEST CASE 2: 2, steven zhang

Pick a category to analyze:
1: Favourite digit
2: Favourite pet
3: Favourite subject
4: Favourite sport to play
5: Favourite sport to watch
6: Favourite music genre
7: Favourite movie genre
8: Favourite fast food place
Enter the NUMBER of the category: 2
Enter the full name of a student (e.g. Evan Chan) who you believe chose the most popular answer : steven zhang
==========================================================================================================================

Number of Votes Each Response Received:

Rabbit : 3
Fish : 3
Dog : 6
Cat : 10
Bird : 2
Reptile : 3

Most popular: Cat with 10 votes
Least popular: Bird with 2 votes

Steven Zhang chose Cat

Steven Zhang's response of Cat was the option with the most votes!
"""
file = open("2.4/responses.csv")
file.readline()

# Give the user categories to choose from
print("Pick a category to analyze:")
print("1: Favourite digit")
print("2: Favourite pet")
print("3: Favourite subject")
print("4: Favourite sport to play")
print("5: Favourite sport to watch")
print("6: Favourite music genre")
print("7: Favourite movie genre")
print("8: Favourite fast food place")


# Looping through the question if they input an invalid response
while True:
    # Ask the user for a category
    category = int(input("Enter the NUMBER of the category: ").strip(".,?! "))
    category += 1
    if 1 < category <= 9:
        break
    else:
        print("Invalid response. Please try again")

# Asking the user for the full name of a student in our class, and defining the variable for their answer
student_name = input("Enter the full name of a student (e.g. Evan Chan) who you believe chose the most popular answer: ").strip(".,?! ").title()
studentAnswer = None

answer_counts = {}
# Loop through each line in the file
for line in file:
    parts = line.strip().split(",")

    answer = parts[category]
    
    # Adding the totals of each option
    if answer in answer_counts:
        answer_counts[answer] += 1
    else:
        answer_counts[answer] = 1

    # Identifies every name in the file
    name = parts[1].strip()

    # Pairing the name chosen with the names answer in the user specified category
    if name.lower() == student_name.lower():
        studentAnswer = answer

# Setting the first answer in the dictionary as the most and least popular
for first_answer in answer_counts:
    most_popular = first_answer
    least_popular = first_answer
    break  

# Going through every option in answer_counts, if the current option is greater than the current most popular than it becomes the most popular, same with the least popular
for option in answer_counts:
    if answer_counts[option] > answer_counts[most_popular]:
        most_popular = option
    if answer_counts[option] < answer_counts[least_popular]:
        least_popular = option

# Print results
print("==========================================================================================================================")
print("\nNumber of Votes Each Response Received:\n")
for option in answer_counts:
    print(option + " : " + str(answer_counts[option]))

print("\nMost popular: " + most_popular + " with " + str(answer_counts[most_popular]) + " votes")
print("Least popular: " + least_popular + " with " + str(answer_counts[least_popular]) + " votes")

# Check if student exists and has a value paired to it
if studentAnswer is not None:
    print("\n" + student_name + " chose " + studentAnswer)
    # Case for if the students answer was the most popular
    if studentAnswer == most_popular:
        print("\nNice Job! " + student_name + "'s response of " + studentAnswer + " was the option with the most votes!")
    else:
        diff = answer_counts[most_popular] - answer_counts[studentAnswer]

        # Case for if the students answer was 1 less than the most popular
        if diff == 1:
            print("\nIt was super close! " + student_name + "'s response of " + studentAnswer + " got " + str(diff) + " less vote than the most popular response, " + most_popular)
            
        # Case for if the students answer was in between 2-4 less than the most popular
        elif 2 <= diff <5:
            print("\nIt was fairly close! " + student_name + "'s response of " + studentAnswer + " got " + str(diff) + " fewer votes than the most popular response, " + most_popular)
            
        # Case for if the students answer was 5 or more votes less than the most popular
        else:
            print("\nIt was not close at all! " + student_name + "'s response of " + studentAnswer + " got " + str(diff) + " fewer votes than the most popular response, " + most_popular)
# If the student inputted is not recognized          
else:
    print("Student not found")


