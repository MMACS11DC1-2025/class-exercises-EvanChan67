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
- Peer review discussion: feedback, code changes made (if a ny), and debugging support

## Project Overview
- My program is a rotating shapes program that takes user input to create a program that takes a shape, and increases its size while rotating it, to create beautiful and abstract patterns. 
- It passes through the function twice: once for the outer layer and again but with less turns for the inner layer. 
- The user decides the shape, the number of levels, and the themes of both layers

## Recursive Approach
- Each recursive call draws one iteration of the pattern (or one full shape)
- After each shape, the turtle turns slightly and makes another recursive call
- The "turn" parameter decreases by 1 each time the function calls itself, to eventually lead to the base case: turns == 0, and exit out of the function
- Because each turn moves the turtle by a specific small angle (calculated by dividing the number of degrees in a circle by the number of turns), the function will always stop when the shapes have reached a full 360 degree rotation from its starting position

## How to run the program
- This program requires a compiler that supports turtle graphics
- Once running, the user should follow the prompts given:
    1. Enter the number of the shape you want to rotate:1) Octagon 2) Hexagon 3) Square 4) Triangle 5) Star
    2. Enter an integer for the amount of levels (1-5): Higher = more dense
    3. Enter the theme for the outer layer: (reds, greens, blues, greys, rainbow)
    4. Enter the theme for the inner layer: (reds, greens, blues, greys, rainbow)
- If an input that was not specified was inputted, the program will keep asking until a valid input was inputted
    - e.g. If "90" is inputted for the first prompt, the program will ask you to answer the question again: Invalid option. Please type an integer from 1-5

## Reasonable Recursion Depth
- The depth of the recursion is controlled by the variable "turns"
- This means each call of the function will result in one more rotation of the shape
- If "turns" is too low(turns<20): The pattern will look incomplete and the recursion will end very quickly, only getting through a few shapes
- If "turns" is too high(turns>300): The performance will decrease significantly and possibly lag. It could also freeze because of the large amount of recursive calls being made 
- A reasonable range for turns is around 60-150, as demonstrated by my use of 90 in the program. This range ensures that the pattern will actually complete a full rotation without any performance/lag issues


