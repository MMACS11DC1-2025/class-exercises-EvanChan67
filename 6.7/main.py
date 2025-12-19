from PIL import Image  
import time            

''' 
Function to determine if the pixel is considered hot
1. Normalize the RGB values to a 0-1 scale
2. Calculate a weighted score based on the RGB values
3. Returns a number from 0-2 indicating the density of the red color.
'''
def is_target_feature(r, g, b):
    # Normalize values to 0-1 for proportional calculation
    r_norm = r / 255
    g_norm = g / 255
    b_norm = b / 255

    # Calculate a weighted score: 
    # Red contributes heavily so its weight more, green and blue contribute negatively indicating cooler colors like yellow/green/blue
    weighted_score = (r_norm * 2.0) - g_norm - b_norm
    
    # Only consider areas that have a positive heat signal
    return max(0.0, weighted_score) 
    # Returns a number (0.0 to approximately 2.0)
'''
Function to analyze every pixel in an image
1. Create a nested for loop to iterate through every pixel
2. Pass the pixel through the is_target_feature function to determine the weight of hot pixels
3. Add the weight to a running total
4. Find the average weighted score to see the density score
5. This function also creates a visual mask of the image to show where the hot pixels are (green for hot, grayscale for cold)
6. Creates a new image file with the mask and saves it
'''
def analyze_image(image_name):
    
    img = Image.open(image_name)
    pixels = img.load()
    width = img.width 
    height = img.height 
    
    # Masked image
    mask_img = img.copy()
    mask_pixels = mask_img.load()

    total_weighted_score = 0.0
    totalpixels = width * height

    for x in range(width):
        for y in range(height):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]

            # Get the weight of the pixel
            pixel_weight = is_target_feature(r, g, b)
            total_weighted_score += pixel_weight

            if pixel_weight > 0:
                # If it has any heat, turn it bright green
                mask_pixels[x, y] = (0, 255, 0)
            else:
                # If it is cold, turn it grayscale so the heat stands out
                avg = int((r + g + b) / 3)
                mask_pixels[x, y] = (avg, avg, avg)
    
    # Save the masked image 
    clean_name = image_name.split('/')[-1] 
    output_filename = "mask_" + clean_name
    mask_img.save(output_filename)
    print("Saved visual map: {}".format(output_filename))

    # Calculate the average weighted score across the image
    density_score = (total_weighted_score / totalpixels) * 100
    return density_score
'''
Selection sort function is used to sort the images by density score from highest to lowest
1. Nested for loop to go through every element and test if the rest of them are larger than it
2. Swap the larger element with the current index
3. Returns the sorted list  
'''
def selection_sort(data_list):
    
    # Traverse through all list elements
    for i in range(len(data_list)):
        # Find the max element in remaining unsorted array
        max_index = i
        for j in range(i + 1, len(data_list)):
            # Compare scores (index 1 of the tuple)
            # Use > because I want to find highest to lowest
            if data_list[j][1] > data_list[max_index][1]:
                max_index = j
                
        # Swap the found maximum element with the first element 
        temp = data_list[i]
        data_list[i] = data_list[max_index]
        data_list[max_index] = temp
        
    return data_list
''' 
Binary search function to search for a specific target value
1. List must be sorted before
2. Find the middle of the list and the boundaries
3. Compare the difference of the guessed score and the current score with the margin of error
4. Return it if it is less than the margin of error
5. Otherwise if the current score is less than the guessed score, the target is in the left half. Vice versa
'''
def binary_search(sorted_list, target_score):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        # Calculate middle index using integer division
        mid = int((low + high)/2)
        mid_score = sorted_list[mid][1]

        # Use a small range for float comparison
        margin_of_error = 1
        
        if abs(mid_score - target_score) < margin_of_error:
            # Target found, return index
            return mid 
        
        # Since the list is sorted from high to low, the logic is reversed
        elif mid_score < target_score:
            # If the middle is lower than target, the target must be in the left half
            high = mid - 1
        else:
            # If the middle is higher than target, the target must be in the right half
            low = mid + 1

    # Target not found        
    return -1 
'''
Main function that contains everything the program does
'''
def main():
    # Images list
    image_files = [
        "6.7/image1.png", "6.7/image2.png", "6.7/image3.png", "6.7/image4.png", "6.7/image5.png",
        "6.7/image6.png", "6.7/image7.png", "6.7/image8.png", "6.7/image9.png", "6.7/image10.png",
    ]
    
    master_list = [] 

    print("\nStarting Image Analysis")
    
    # start timer
    start_time1 = time.time()

    # Loop through the list of images
    for img_name in image_files:
        print("Processing " + img_name + "...") 
        score = analyze_image(img_name)
        
        # Append image_name and score to master list 
        master_list.append((img_name, score))

    # end timer
    end_time1 = time.time()
    total_time1 = end_time1 - start_time1
    print("-" * 30)
    print("\nProcessing Complete.")
    print("Time taken: {:.3f} seconds".format(total_time1))
    print("-" * 30)

    # Sort the results
    print("\nSorting results by Heat Density (Highest to Lowest)...")
    start_time2 = time.time()
    sorted_list = selection_sort(master_list)
    end_time2 = time.time()
    total_time2 = end_time2 - start_time2
    print("Sorting complete. Time taken to sort: {: .3f} seconds".format(total_time2))
    print("-" * 30)

    # Output top 5 results using list slicing
    print("\nTop 5 Hottest Images:")
    top_5 = sorted_list[:5]
    for item in top_5:
        # Accessing tuple elements by index 
        print("File: {} | Score: {:.2f}".format(item[0], item[1]))
    print("-" * 30)
    
    # Binary Search Test
    search_target = usertarget
    print("\nSearching for image with score approximately {:.2f}...".format(search_target))
    start_time3 = time.time() 
    found_index = binary_search(sorted_list, search_target)
    end_time3 = time.time()
    total_time3 = end_time3 - start_time3
    print("Searching complete. Time taken to search: {: .3f} seconds".format(total_time3))

    if found_index != -1:
        print("Found at index {}: {}".format(found_index, sorted_list[found_index]))
    else:
        print("No image found with that exact score.")

# User input and start
while True:
    try: 
        usertarget = float(input("Guess a rational number (1-100) for a density score ").strip(".!?, "))
    except:
        print("Invalid input. Input a DECIMAL")
    else:
        if 0 <= usertarget <= 100:
            main()
            break
        else:
          print("Invalid input. Input a number from the range 1-100")          
