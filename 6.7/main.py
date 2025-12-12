from PIL import Image  
import time            

def is_target_feature(r, g, b):
    
    # In the heat map, hot areas are usually red or orange 
    if r > 160 and b < 100:
        return True
    else:
        return False

def analyze_image(image_name):

    # Initializing the image, pixels, width and height, and total pixels
    img = Image.open(image_name)

    pixels = img.load()
    
    width = img.width  
    height = img.height 
    
    hotpixels = 0
    totalpixels = width * height

    # Nested loops to iterate over x (width) and y (height) 
    for x in range(width):
        for y in range(height):
            # pixels[x, y] returns a tuple (r, g, b)
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]
            
            # Check if this pixel matches the feature
            if is_target_feature(r, g, b):
                hotpixels += 1
    
    # Calculate what percentage of the area is hot
    # Multiply by 100 to get a clean number 
    density_score = (hotpixels / totalpixels) * 100
    return density_score

def selection_sort(data_list):
    
    n = len(data_list)
    
    # Traverse through all list elements
    for i in range(n):
        # Find the max element in remaining unsorted array
        max_index = i
        for j in range(i + 1, n):
            # Compare scores (index 1 of the tuple)
            # Use > because I want to find highest to lowest
            if data_list[j][1] > data_list[max_index][1]:
                max_index = j
                
        # Swap the found maximum element with the first element 
        temp = data_list[i]
        data_list[i] = data_list[max_index]
        data_list[max_index] = temp
        
    return data_list

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
            return mid # Target found, return index
        
        # Since the list is sorted from high to low, the logic is reversed
        elif mid_score < target_score:
            # If the middle is lower than target, the target must be in the left half
            high = mid - 1
        else:
            # If the middle is higher than target, the target must be in the right half
            low = mid + 1

    # Target not found        
    return -1 

def main():
    # Images list
    image_files = [
        "6.7/image1.png", "6.7/image2.png", "6.7/image3.png", "6.7/image4.png", "6.7/image5.png",
        "6.7/image6.png", "6.7/image7.png", "6.7/image8.png", "6.7/image9.png", "6.7/image10.png",
    ]
    
    master_list = [] 

    print("\n--- Starting Image Analysis ---")
    
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
        usertarget = float(input("Input a rational number (1-100) for a density score ").strip(".!?, "))
    except:
        print("Invalid input. Input a DECIMAL")
    else:
        if 0 <= usertarget <=100:
            main()
            break
        else:
          print("Invalid input. Input a number from the range 1-100")  
        
        
