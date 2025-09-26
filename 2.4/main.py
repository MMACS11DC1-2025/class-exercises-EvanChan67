responses = open("2.4/responses.csv")
for response in responses:
    response = response.split(",")
    if response[1] == "Evan Chan":      
        print(response)