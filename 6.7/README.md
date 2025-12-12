### Image Explorer Project
## Evan Chan 


## Project Overview
- For my project, I decided to choose the theme of satellite photos measuring average temperatures at specific regions of the earth (Canada, Southern North America, South America, Africa, Europe, Russia, East Asia, South-East Asia, Australia, the Middle East)
- My program will detect how close to red a pixel is to determine how hot that specific pixel is (redder=hotter). It searches every pixel and in the end, calculates the average density of warm pixels, or percentage of warm pixels to the total. After, it sorts the images from highest to lowest density score to determine the hottest region
- This feature detection can accurately identify the heat density of the image because the images that were chosen to be analyzed were all taken from the official earths temperature forecast website, "https://zoom.earth/maps/temperature/". This website pulls data from the latest global model data from DWD ICON and NOAA/NCEP/NWS and uses it to classify temperatures on the colour scale that i based my project on

## Testing and Validation
- I tested the is_target_feature() function using individual RGB values to confirm that it correctly classified hot pixels and rejected cooler ones
- I also tested edge cases such as extremely dark images and images with very little red content to confirm that the function never crashes and always returns a valid percentage.
- The sorting and searching functions were tested with artificial sample lists before being used on the real dataset to ensure that they correctly handled highest to lowest sorting and float based search comparisons.

## Code Profiling
- Analyzing image test times: 1.261, 1.306, 1.265, 1.268, 1.472
- Average: 1.314s
- Average for sorting and searching: 0.000s
- On average, analyzing all 10 images required approximately 1.314 seconds. This profiling showed that:
- The pixel-iteration loops are the slowest part of the program, since every single pixel of every image must be checked individually.
- Sorting and searching take significantly less time because the lists involved are small compared to the pixel count.
- Overall, the runtime is efficient for the image sizes used

## Challenges
- One challenge I faced was creating a feature detection rule that works for every image. Originally, the thresholds for red and blue were too strict, which caused some correctly hot areas to be missed. I solved this by adjusting and testing multiple RGB boundaries until I found values that correctly captured the visual feature.
- Another challenge involved handling the sorting order. Since selection sort normally finds the minimum value, I had to reverse the comparison so that the algorithm sorted the results from highest to lowest, matching the project requirements.
- Lastly, comparing floating point numbers in the binary search required using a small margin of error instead of checking for exact equality. Without this, the search function would fail even if the value was extremely close.