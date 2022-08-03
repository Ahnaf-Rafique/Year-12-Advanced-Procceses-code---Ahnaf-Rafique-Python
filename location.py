#Input

#location
def location_checker(question):

    valid = False
    while not valid:

        #ask user for choice
        response = input(question)

        if response == list_of_location:
            return response

#output
user_choice = location_checker("choose your location: ")
list_of_location = ["sandrigham" , "mangere" , "henderson" , "mount albert" , "mount roskill" , "auckland" , "newmarket" , "mount eden"]

list1 = [1,sandrigham  , 2 ,mangere , 3 , henderson, 4 , mount albert, 5 , "mount roskill"]
for index, item in enumerate(list1):
    print(item, index)