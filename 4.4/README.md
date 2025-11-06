# Rotating Shapes Program- Evan Chan

### **Required Documentation Content Summary:**
- Project overview
- Explanation of your recursive approach and why it works
- How to run the program
- Screenshots of visual outputs (at least 2 different results)
- Test cases with expected vs actual results
- Discussion of reasonable recursion depth (why too low/high won't work)
- Discuss performance implications of different depths
- Suggest reasonable range for your implementation
- Testing, debugging, and validation process documentation
- Peer review discussion: feedback, code changes made (if any), and debugging support

## Project Overview
- My program is a rotating shapes program that takes user input to create a program that takes a shape, and increases its size while rotating it, to create beautiful and abstract patterns. 
- It passes through the function twice: once for the outer layer and again but with less turns for the inner layer. 
- The user decides the shape, the number of levels/density, and the themes of both layers

## Recursive Approach
- Each recursive call draws one iteration of the pattern (or one full shape)
- After each shape, the turtle turns slightly and makes another recursive call
- The "turn" parameter decreases by 1 each time the function calls itself to eventually lead to the base case: turns == 0, and exit out of the function
- Because each turn moves the turtle by a specific small angle (calculated by dividing the number of degrees in a circle by the number of turns), the function will always stop when the shapes have reached a full 360 degree rotation from its starting position

## How to run the program
- This program requires a compiler that supports turtle graphics
- Once running, the user should follow the prompts given:
    1. Enter an integer of the shape you want to rotate:1) Octagon 2) Hexagon 3) Square 4) Triangle 5) Star
    2. Enter an integer for the amount of levels (1-5): Higher = more dense
    3. Enter the theme for the outer layer: (reds, greens, blues, greys, rainbow)
    4. Enter the theme for the inner layer: (reds, greens, blues, greys, rainbow)
- If an input that was not specified was inputted, the program will keep asking until a valid input was inputted
    - e.g. If "6" is inputted for the first prompt, the program will ask you to answer the question again: Invalid option. Please type an integer from 1-5

## More about the program
### Inputs on Outputs
- For the first prompt, it asks the user for an integer from 1-5. Each number corresponds to a "shape". This shape is actually just created by changing the angle in which the turtle rotates after every line. So if the user inputs 3 (which corresponds to the square), the turtle would rotate to the left 90 degrees, creating the square shape the user sees
- For the second prompt, it asks the user for an integer from 1-5. These values correspond to a different level/density of the drawing. The parameter "levels" is used in the main for loop for the amount of times that the turtle would draw a shape, thus creating a denser look for larger values passed
- For the third and fourth inputs, it asks the user for the colour themes of the outer and inner layer. The value that the user inputs corresponds to a key in the dictionary created at the top. That key holds a list of colour values that would later be used when drawing the shapes.

## Screenshots
### The first two screenshots below show the difference between a level 1 triangle and a level 5 triangle
- Input = 4, 1, reds, blues 
- ![alt text](image-1.png)

- Input = 4, 5, blues, reds
- ![alt text](image-2.png)

### Misc.
- Input = 2, 1, greys, rainbow
- ![alt text](image-3.png)

- Input = 5, 4, greens, blues
- ![alt text](image-4.png)

## Test cases
- Input = 2, 1, reds, rainbow
- Expected output = a red hexagon rotating and growing larger every single rotation, then a rainbow hexagon doing the same but on top of it and ending sooner. Also returns the total number of recursive calls
- Actual output = a red hexagon rotating and growing larger every single rotation, then a rainbow hexagon doing the same but on top of it and ending sooner. Also returns the total number of recursive calls of 150
- Expected and Actual output is the exact same

- Input = 5, 5, blues, greens
- Expected output = blue star rotating and growing larger every rotation, very dense/rotates alot more times. Same for greens, but ends sooner. Also returns the total number of recursive calls
- Actual output = blue star rotating and growing larger every rotation, very dense/rotates alot more times. Same for greens, but ends sooner. Also returns the total number of recursive calls of 150
- Exected and Actual output is the exact same


## Reasonable Recursion Depth
- The depth of the recursion is controlled by the variable "turns"
- This means each call of the function will result in one more rotation of the shape
- If "turns" is too low(turns<20): The pattern will look incomplete and the recursion will end very quickly, only getting through a few shapes
- If "turns" is too high(turns>250): The performance will decrease significantly and possibly lag. It could also freeze because of the large amount of recursive calls being made 
- A reasonable range for turns is around 60-150, as demonstrated by my use of 90 in the program. This range ensures that the pattern will actually complete a full rotation without any performance/lag issues

## Testing Debugging and Validation
1. Verified that the recursion actually terminated when turns == 0
2. Implemented while loops to ensure all user inputs were valid
3. Colour index was going out of range and erroring originally, so an if statement was used to reset the index back to 0 every time it reached the end of the colour list
4. Ran multiple tests to make sure that the different combinations of shapes and levels worked to rotate around a full circle
5. Added return values to count and confirm the amount of recursive calls made

## Peer Review
### Suggestions:
- Add error handling code, if the user inputs something that isnt supported
- Add more colours
### Changes made:
- Created while loops to repeatedly ask the user the question if unsupported value was passed
- Added a wider range of colour choices to choose from (greys and rainbow)

