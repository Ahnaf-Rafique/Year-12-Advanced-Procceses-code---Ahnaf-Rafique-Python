#dictionary
#locations within the dictionary

dict_suburb = { "Sandrigham" : "Life Wise Health And Disability Services",
    "Newmarket" : "Salvation Army Epsom Lodge, Ronald Mcdonald House, Life Wise, Auckland Mission",
    "Grey_Lynn" : "Youth Line, James Liston Hotel",
    "Avondale" : "Housing First, Monte Cilla Housing Trust",
    "Mangere" : "Mangere East Family Service",
    "Manukau" : "Youth Line Manukau, New Zealand Red Cross, Salvation Army"
               }

location = True

#prompt user for location
while location:
    Location = input("Enter your location your location: ")

     #store the response in a dictionary
   # Location = Sandrigham , Newmarket , Grey_Lynn , Avondale , Mangere , Manukau
    if Location in dict_suburb.keys():
        print(dict_suburb.values())





